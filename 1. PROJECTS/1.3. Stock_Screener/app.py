import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from core import (
    normalize_symbols,
    build_features_dataframe,
    score_symbols,
    get_price_history
)


st.set_page_config(
    page_title="Stock Screener",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    .stApp {
        background-color: #f8fafc;
    }
    .main-title {
        font-size: 58px;
        font-weight: 800;
        background: linear-gradient(90deg, #e83e8c, #7c3aed, #db2777);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 20px 0 10px 0;
        letter-spacing: -2px;
    }
    .subtitle {
        text-align: center;
        font-size: 22px;
        color: #475569;
        margin-bottom: 40px;
        font-weight: 400;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }

    /* Button */
    .stButton>button {
        background: linear-gradient(90deg, #e83e8c, #db2777) !important;
        color: white !important;
        font-weight: 700;
        font-size: 19px;
        height: 58px;
        border-radius: 14px !important;
        box-shadow: 0 6px 16px rgba(232, 62, 140, 0.35);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(232, 62, 140, 0.45);
    }

    /* Result Cards */
    .result-card {
        background: white;
        padding: 28px;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.07);
        border: 1px solid #f1f5f9;
        margin-bottom: 30px;
    }

    /* Dataframe */
    .stDataFrame {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.06);
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 40px 0 25px;
        color: #64748b;
        font-size: 14.5px;
        border-top: 1px solid #e2e8f0;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# ====================== SIDEBAR ======================
st.sidebar.header("⚙️ Tham số phân tích")

symbols_text = st.sidebar.text_area(
    "Danh sách mã cổ phiếu",
    value="ACB, VNM, HPG, FPT, MWG",
    height=130
)

days = st.sidebar.number_input("Số ngày lịch sử giá", value=270, min_value=120, max_value=730, step=30)
min_adtv = st.sidebar.number_input("Ngưỡng thanh khoản tối thiểu (tỷ VND/ngày)", value=50, min_value=5, step=5)

analyze_btn = st.sidebar.button(" Phân tích ngay", type="primary", use_container_width=True)

# ====================== MAIN CONTENT ======================
st.markdown('<div class="main-title">🌸 Stock Screener</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Công cụ sàng lọc cổ phiếu theo mô hình đa yếu tố</div>', unsafe_allow_html=True)

if analyze_btn:
    symbols = normalize_symbols(symbols_text)
    
    if not symbols:
        st.error("Vui lòng nhập ít nhất một mã cổ phiếu!")
        st.stop()

    with st.spinner("Đang lấy dữ liệu và phân tích..."):
        df_features = build_features_dataframe(symbols, days)
        ranked = score_symbols(df_features, min_adtv_billion=min_adtv)

    if ranked.empty:
        st.warning("Không có mã nào đủ ngưỡng thanh khoản. Hãy thử giảm ngưỡng.")
        st.stop()

    # Bảng xếp hạng
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.subheader("🏆 Bảng xếp hạng")
    st.dataframe(
        ranked.style.format({
            "score": "{:.4f}",
            "Value": "{:.3f}", "Quality": "{:.3f}", "Growth": "{:.3f}",
            "Momentum": "{:.3f}", "Liquidity": "{:.3f}", "RiskAdj": "{:.3f}"
        }),
        use_container_width=True,
        height=420
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Top Pick
    best = ranked.iloc[0]
    st.success(f"""
    **{best['symbol']}** là mã phù hợp nhất trong danh sách đầu vào.  
    Điểm tổng: **{best['score']:.4f}** | Thanh khoản trung bình: **{best.get('adtv_billion', 0):.1f} tỷ/ngày**
    """)

    # Biểu đồ
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.subheader("📊 Biểu đồ giá & khối lượng ")
    
    for sym in ranked["symbol"].head(5):
        px = get_price_history(sym, days)
        if px.empty:
            continue
            
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(10, 5.2))
            ax.plot(px["date"], px["close"], color="#e83e8c", linewidth=3.5)
            ax.set_title(f"{sym} — Giá đóng cửa", fontsize=16, pad=18)
            ax.set_xlabel("Ngày")
            ax.set_ylabel("Giá (VND)")
            ax.grid(True, alpha=0.25)
            plt.xticks(rotation=45, ha='right')
            fig.autofmt_xdate()
            st.pyplot(fig)
            plt.close(fig)

        with col2:
            fig2, ax2 = plt.subplots(figsize=(10, 5.2))
            ax2.bar(px["date"], px["volume"], color="#14b8a6", alpha=0.92)
            ax2.set_title(f"{sym} — Khối lượng khớp", fontsize=16, pad=18)
            ax2.set_xlabel("Ngày")
            ax2.set_ylabel("Khối lượng")
            ax2.grid(True, alpha=0.25)
            plt.xticks(rotation=45, ha='right')
            fig2.autofmt_xdate()
            st.pyplot(fig2)
            plt.close(fig2)
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("👈 Nhập danh sách mã ở sidebar và nhấn **Phân tích ngay** để bắt đầu.")


# ====================== FOOTER ======================
st.markdown("""
<div class="footer">
    <p><strong>Developed by Minh Thảo</strong></p>
    <p>
        📘 <a href="https://www.facebook.com/share/1CH6B1QTNw/?mibextid=wwXIfr" target="_blank" style="color:#e83e8c; text-decoration:none; font-weight:500;">
            Facebook
        </a> &nbsp;&nbsp; • &nbsp;&nbsp; 
        📱 Zalo: <strong>0769 511 620</strong>
    </p>
    <p style="margin-top:18px; font-size:13.5px; color:#94a3b8;">
        (*)Đây là dự án phục vụ mục đích học tập và nghiên cứu. Không phải khuyến nghị đầu tư.
    </p>
</div>
""", unsafe_allow_html=True)