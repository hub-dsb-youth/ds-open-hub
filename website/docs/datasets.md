---
sidebar_position: 3
---

# Datasets

Danh mục dữ liệu trong DS Open Hub tập trung vào các bài toán churn, marketing, retail và time series.

## Nhóm Bank Marketing

- 3.1 Dataset Bank Marketing
- 3.3 Dataset Tiếp thị ngân hàng
- Lưu ý: dữ liệu mất cân bằng nhãn, cần ưu tiên đánh giá precision, recall, F1, AUC

## Nhóm Customer Churn

- 3.7 Customer Churn
- Dùng cho bài toán classification và chiến lược giữ chân khách hàng

## Nhóm Time Series và Thị trường

- 3.4 Giá dầu 1970-2026
- 3.5 FPT
- 3.6 HPG
- Lưu ý: tách train/test theo thời gian, tránh random split

## Nhóm Retail

- 3.2 Online Retail
- Dùng cho doanh thu theo thời gian, RFM, phân cụm khách hàng, market basket

## Best practices khi làm việc với dữ liệu

1. Kiểm tra missing, duplicate và outlier trước khi modeling.
2. Chuẩn hóa kiểu dữ liệu thời gian và phân tách train/test đúng ngữ cảnh bài toán.
3. Với dữ liệu mất cân bằng, tránh chỉ dùng accuracy để kết luận mô hình.
