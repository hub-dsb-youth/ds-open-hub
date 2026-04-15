# 3.6. HPG

## Mô tả dữ liệu

Bộ dữ liệu lịch sử giao dịch cổ phiếu HPG đã qua tiền xử lý cơ bản, phù hợp cho bài toán phân tích kỹ thuật và dự báo giá theo thời gian.

## Thông tin tệp dữ liệu

- Tệp dữ liệu: HPG_clean.csv
- Số dòng: 2,000
- Số cột: 13
- Khoảng thời gian: 2018-03-22 đến 2026-03-27
- Mã cổ phiếu: HPG

## Data Dictionary

- Ngay: ngày giao dịch
- GiaMoCua, GiaDongCua, GiaCaoNhat, GiaThapNhat: nhóm giá trong phiên
- GiaDieuChinh: giá đã điều chỉnh
- KhoiLuongKhopLenh, GiaTriKhopLenh: thanh khoản thị trường
- symbol: mã cổ phiếu
- ThayDoi_Gia, ThayDoi_PhanTram: biến động giá theo ngày
- EMA_20: chỉ báo xu hướng ngắn hạn
- RSI_14: chỉ báo động lượng

## Lưu ý phân tích

- Cần đảm bảo dữ liệu được sắp xếp tăng dần theo Ngay trước khi train mô hình.
- Nên tách tập train/test theo thời gian (time-based split), tránh random split.
- Có thể tạo thêm feature lag (t-1, t-5, t-20) để cải thiện dự báo ngắn hạn.

## Bài toán phù hợp

- EDA về biến động giá, thanh khoản và độ biến động theo giai đoạn.
- Dự báo GiaDongCua/GiaDieuChinh bằng các mô hình time series.
- Thử nghiệm chiến lược cảnh báo quá mua/quá bán dựa trên RSI.
