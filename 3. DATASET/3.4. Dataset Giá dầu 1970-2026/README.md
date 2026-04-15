# 3.4. Dataset Giá dầu 1970-2026

## Mô tả dữ liệu

Bộ dữ liệu ghi nhận biến động giá dầu theo chuỗi thời gian dài hạn, phù hợp cho bài toán time series và phân tích xu hướng năng lượng.

## Thông tin tệp dữ liệu

- Tệp dữ liệu: fuel_prices_1970_2026.csv
- Số dòng: 675
- Số cột: 2
- Khoảng thời gian: 1970-01-01 đến 2026-03-01

## Data Dictionary

- Date: mốc thời gian quan sát
- Crude_Oil_Price: giá dầu thô tại thời điểm tương ứng

## Đặc điểm dữ liệu

- Cấu trúc đơn giản, dễ triển khai trực quan hóa và forecasting cơ bản.
- Chuỗi dữ liệu dài hạn giúp quan sát cả xu hướng dài hạn và các giai đoạn biến động mạnh.
- Có thể kết hợp với dữ liệu kinh tế vĩ mô (lãi suất, lạm phát, GDP) để mở rộng phân tích.

## Bài toán phù hợp

- Dự báo chuỗi thời gian (ARIMA/Prophet/LSTM).
- Phát hiện điểm gãy (structural break) và các cú sốc giá năng lượng.
- Trực quan hóa xu hướng giá dầu theo giai đoạn.
