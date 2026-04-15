---
sidebar_position: 3
---

# Datasets

Danh mục dữ liệu trong DS Open Hub tập trung vào các bài toán churn, marketing, retail và time series.

## Quick Links

- [Open 3. DATASET folder](https://github.com/hub-dsb-youth/ds-open-hub/tree/main/3.%20DATASET)
- [Download full repository (.zip)](https://github.com/hub-dsb-youth/ds-open-hub/archive/refs/heads/main.zip)

## Nhóm Bank Marketing

- 3.1 Dataset Bank Marketing
- 3.3 Dataset Tiếp thị ngân hàng
- Lưu ý: dữ liệu mất cân bằng nhãn, cần ưu tiên đánh giá precision, recall, F1, AUC

Links:

- [3.1 README](https://github.com/hub-dsb-youth/ds-open-hub/blob/main/3.%20DATASET/3.1.%20Dataset%20Bank%20Marketing/README.md)
- [3.1 CSV download](https://github.com/hub-dsb-youth/ds-open-hub/blob/main/3.%20DATASET/3.1.%20Dataset%20Bank%20Marketing/3.1%20Dataset%20Bank%20Marketing%20.csv?raw=1)
- [3.3 README](https://github.com/hub-dsb-youth/ds-open-hub/blob/main/3.%20DATASET/3.3.%20Dataset%20Ti%E1%BA%BFp%20th%E1%BB%8B%20ng%C3%A2n%20h%C3%A0ng/README.md)
- [3.3 CSV download](https://github.com/hub-dsb-youth/ds-open-hub/blob/main/3.%20DATASET/3.3.%20Dataset%20Ti%E1%BA%BFp%20th%E1%BB%8B%20ng%C3%A2n%20h%C3%A0ng/bank-additional-full.csv?raw=1)

## Nhóm Customer Churn

- 3.7 Customer Churn
- Dùng cho bài toán classification và chiến lược giữ chân khách hàng

Links:

- [3.7 README](https://github.com/hub-dsb-youth/ds-open-hub/blob/main/3.%20DATASET/3.7.%20Customer%20Churn/README.md)
- [3.7 CSV download](https://github.com/hub-dsb-youth/ds-open-hub/blob/main/3.%20DATASET/3.7.%20Customer%20Churn/customer_churn.csv?raw=1)

## Nhóm Time Series và Thị trường

- 3.4 Giá dầu 1970-2026
- 3.5 FPT
- 3.6 HPG
- Lưu ý: tách train/test theo thời gian, tránh random split

Links:

- [3.4 CSV download](https://github.com/hub-dsb-youth/ds-open-hub/blob/main/3.%20DATASET/3.4.%20Dataset%20Gi%C3%A1%20d%E1%BA%A7u%201970-2026/fuel_prices_1970_2026.csv?raw=1)
- [3.5 CSV download](https://github.com/hub-dsb-youth/ds-open-hub/blob/main/3.%20DATASET/3.5.%20FPT/FPT_clean.csv?raw=1)
- [3.6 CSV download](https://github.com/hub-dsb-youth/ds-open-hub/blob/main/3.%20DATASET/3.6.%20HPG/HPG_clean.csv?raw=1)

## Nhóm Retail

- 3.2 Online Retail
- Dùng cho doanh thu theo thời gian, RFM, phân cụm khách hàng, market basket

Links:

- [3.2 README](https://github.com/hub-dsb-youth/ds-open-hub/blob/main/3.%20DATASET/3.2.%20Dataset%20Online%20Retail/README.md)

## Best practices khi làm việc với dữ liệu

1. Kiểm tra missing, duplicate và outlier trước khi modeling.
2. Chuẩn hóa kiểu dữ liệu thời gian và phân tách train/test đúng ngữ cảnh bài toán.
3. Với dữ liệu mất cân bằng, tránh chỉ dùng accuracy để kết luận mô hình.
