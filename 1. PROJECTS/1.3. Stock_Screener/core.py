import io
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List

import numpy as np
import pandas as pd
from vnstock import Vnstock


try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
except Exception:
    pass


def _prev_weekday(dt: datetime) -> datetime:
    while dt.weekday() >= 5:
        dt -= timedelta(days=1)
    return dt


def _to_numeric(value):
    return pd.to_numeric(value, errors="coerce")


def normalize_symbols(symbols_text: str) -> List[str]:
    if not symbols_text:
        return []
    parts = [x.strip().upper() for x in symbols_text.replace("\n", ",").split(",")]
    return [x for x in parts if x and len(x) >= 3]


# ====================== LẤY DỮ LIỆU ======================
def get_price_history(symbol: str, days: int = 270) -> pd.DataFrame:
    try:
        end_dt = _prev_weekday(datetime.today())
        start_date = (end_dt - timedelta(days=int(days * 2))).strftime("%Y-%m-%d")
        end_date = end_dt.strftime("%Y-%m-%d")

        stock = Vnstock().stock(symbol=symbol.upper(), source="VCI")
        df = stock.quote.history(start=start_date, end=end_date, interval="1D")

        if df is None or df.empty:
            return pd.DataFrame()

        df = df.copy()

        # Chuẩn hóa tên cột
        rename_map = {}
        for c in df.columns:
            cl = str(c).lower()
            if cl in ["time", "tradingdate", "date"]:
                rename_map[c] = "date"
            elif cl in ["close", "closeprice", "matchprice"]:
                rename_map[c] = "close"
            elif cl in ["volume", "matchvolume", "totalvolume"]:
                rename_map[c] = "volume"
        df = df.rename(columns=rename_map)

        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["close"] = _to_numeric(df.get("close"))
        df["volume"] = _to_numeric(df.get("volume"))

        df = df[["date", "close", "volume"]].dropna(subset=["close"]).sort_values("date").reset_index(drop=True)
        return df
    except Exception:
        return pd.DataFrame()


def get_fundamentals(symbol: str) -> Dict:
    result = {"pe": np.nan, "pb": np.nan, "roe": np.nan, "de": np.nan, "net_margin": np.nan, "rev_yoy": np.nan, "eps_yoy": np.nan}
    try:
        stock = Vnstock().stock(symbol=symbol.upper(), source="VCI")
        f = getattr(stock, "finance", None)
        if f is None:
            return result
        ratios = f.ratios()
        if ratios is None or ratios.empty:
            return result
        latest = ratios.iloc[0].to_dict()
        result["pe"] = _to_numeric(latest.get("PE") or latest.get("P/E"))
        result["pb"] = _to_numeric(latest.get("PB") or latest.get("P/B"))
        result["roe"] = _to_numeric(latest.get("ROE"))
        result["de"] = _to_numeric(latest.get("D/E") or latest.get("Debt/Equity"))
        return result
    except Exception:
        return result


def compute_features(symbol: str, days: int = 270) -> Dict:
    px = get_price_history(symbol, days)
    empty = {"symbol": symbol.upper(), "m1": np.nan, "m3": np.nan, "m6": np.nan, "adtv": np.nan, "vol": np.nan,
             "pe": np.nan, "pb": np.nan, "roe": np.nan, "de": np.nan, "net_margin": np.nan, "rev_yoy": np.nan, "eps_yoy": np.nan}

    if px.empty or len(px) < 30:
        return empty

    close = _to_numeric(px["close"])
    m1 = (close.iloc[-1] - close.iloc[-22]) / close.iloc[-22] if len(close) > 22 else np.nan
    m3 = (close.iloc[-1] - close.iloc[-63]) / close.iloc[-63] if len(close) > 63 else np.nan
    m6 = (close.iloc[-1] - close.iloc[-127]) / close.iloc[-127] if len(close) > 127 else np.nan

    last20 = px.tail(20)
    adtv = (_to_numeric(last20["close"]) * 1000 * _to_numeric(last20["volume"])).mean()

    returns = close.pct_change().dropna()
    vol = returns.std() * (252**0.5) if len(returns) >= 2 else np.nan

    f = get_fundamentals(symbol)

    return {**empty, "m1": m1, "m3": m3, "m6": m6, "adtv": adtv, "vol": vol,
            "pe": f["pe"], "pb": f["pb"], "roe": f["roe"], "de": f["de"]}


def build_features_dataframe(symbols: List[str], days: int = 270) -> pd.DataFrame:
    rows = [compute_features(sym, days) for sym in symbols]
    return pd.DataFrame(rows)


# ====================== SCORING ======================
@dataclass
class ScoreWeights:
    value: float = 0.22
    quality: float = 0.22
    growth: float = 0.20
    momentum: float = 0.20
    liquidity: float = 0.10
    risk: float = 0.06


def _winsorize(s: pd.Series, p=0.02):
    s = _to_numeric(s)
    if s.dropna().empty:
        return s
    try:
        return s.clip(lower=s.quantile(p), upper=s.quantile(1 - p))
    except:
        return s


def _zscore(s: pd.Series):
    s = _to_numeric(s).astype(float)
    valid = s.dropna()
    if len(valid) <= 1:
        return pd.Series(0.0, index=s.index)
    sd = valid.std(ddof=0)
    if pd.isna(sd) or sd == 0:
        return pd.Series(0.0, index=s.index)
    return (s - valid.mean()) / sd


def score_symbols(df: pd.DataFrame, min_adtv_billion: float = 20) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    d = df.copy()
    for col in ["m1", "m3", "m6", "adtv", "vol", "pe", "pb", "roe", "de", "net_margin", "rev_yoy", "eps_yoy"]:
        if col in d.columns:
            d[col] = _to_numeric(d[col])

    min_vnd = min_adtv_billion * 1_000_000_000
    d = d[d["adtv"].fillna(0) >= min_vnd].copy()

    if d.empty:
        return pd.DataFrame()

    score_map = [("pe", -1), ("pb", -1), ("roe", 1), ("net_margin", 1), ("de", -1),
                 ("rev_yoy", 1), ("eps_yoy", 1), ("m1", 1), ("m3", 1), ("m6", 1),
                 ("adtv", 1), ("vol", -1)]

    for col, sign in score_map:
        if col not in d.columns:
            d[f"z_{col}"] = 0.0
            continue
        s = _to_numeric(d[col])
        d[f"z_{col}"] = sign * _zscore(_winsorize(s))

    d["Value"] = (d.get("z_pe", 0) + d.get("z_pb", 0)) / 2
    d["Quality"] = (d.get("z_roe", 0) + d.get("z_net_margin", 0) + d.get("z_de", 0)) / 3
    d["Growth"] = (d.get("z_rev_yoy", 0) + d.get("z_eps_yoy", 0)) / 2
    d["Momentum"] = (d.get("z_m1", 0) + d.get("z_m3", 0) + d.get("z_m6", 0)) / 3
    d["Liquidity"] = d.get("z_adtv", 0)
    d["RiskAdj"] = d.get("z_vol", 0)

    w = ScoreWeights()
    d["score"] = (w.value * d["Value"] + w.quality * d["Quality"] + w.growth * d["Growth"] +
                  w.momentum * d["Momentum"] + w.liquidity * d["Liquidity"] + w.risk * d["RiskAdj"])

    d = d.sort_values("score", ascending=False).reset_index(drop=True)
    d["adtv_billion"] = (d["adtv"] / 1_000_000_000).round(1)
    d["m1_pct"] = (d["m1"] * 100).round(1)
    d["m3_pct"] = (d["m3"] * 100).round(1)

    return d