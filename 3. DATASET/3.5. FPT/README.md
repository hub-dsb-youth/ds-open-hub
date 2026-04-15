# 3.5. FPT

## Mô tả dữ liệu

Bộ dữ liệu lịch sử giao dịch cổ phiếu FPT đã được làm sạch cơ bản và bổ sung một số chỉ báo kỹ thuật để phục vụ phân tích và dự báo.

## Thông tin tệp dữ liệu

- Tệp dữ liệu: FPT_clean.csv
- Số dòng: 2,000
- Số cột: 13
- Khoảng thời gian: 2018-03-22 đến 2026-03-27
- Mã cổ phiếu: FPT

## Data Dictionary

- Ngay: ngày giao dịch
- GiaMoCua, GiaDongCua, GiaCaoNhat, GiaThapNhat: nhóm giá trong phiên
- GiaDieuChinh: giá đã điều chỉnh sau sự kiện doanh nghiệp
- KhoiLuongKhopLenh, GiaTriKhopLenh: chỉ số thanh khoản
- symbol: mã cổ phiếu
- ThayDoi_Gia, ThayDoi_PhanTram: biến động so với phiên trước
- EMA_20: exponential moving average 20 phiên
- RSI_14: relative strength index 14 phiên

## Lưu ý phân tích

- Đây là dữ liệu theo ngày giao dịch, cần sắp xếp theo Ngay trước khi tạo feature lag/rolling.
- Các chỉ báo EMA_20 và RSI_14 đã tồn tại sẵn trong dữ liệu, giúp giảm công tiền xử lý.
- Nên kiểm tra stationarity (ADF test) trước khi áp dụng mô hình time series truyền thống.

## Bài toán phù hợp

- EDA về xu hướng giá và thanh khoản cổ phiếu FPT.
- Dự báo GiaDongCua bằng ARIMA/Prophet/XGBoost/LSTM.
- Tạo chiến lược giao dịch đơn giản dựa trên EMA/RSI.
