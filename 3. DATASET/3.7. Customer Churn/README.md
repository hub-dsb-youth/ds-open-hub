# 3.7. Customer Churn

## Mô tả dữ liệu

Bộ dữ liệu mô phỏng hành vi khách hàng trong mô hình dịch vụ (SaaS/B2B), phục vụ bài toán dự đoán churn và phân tích giữ chân khách hàng.

## Thông tin tệp dữ liệu

- Tệp dữ liệu: customer_churn.csv
- Số dòng: 900
- Số cột: 10
- Biến mục tiêu: Churn (0/1)
- Phân bố nhãn:
	- Churn = 1: 150 (~16.67%)
	- Churn = 0: 750 (~83.33%)
- Khoảng onboarding: 2006-01-02 đến 2016-12-28

## Data Dictionary

- Names: tên khách hàng
- Age: độ tuổi
- Total_Purchase: tổng giá trị giao dịch/mua dịch vụ
- Account_Manager: có nhân viên quản lý tài khoản (1) hay không (0)
- Years: số năm sử dụng dịch vụ
- Num_Sites: số site/chi nhánh sử dụng
- Onboard_date: ngày bắt đầu sử dụng dịch vụ
- Location: vị trí/trụ sở khách hàng
- Company: tên công ty
- Churn: biến mục tiêu rời bỏ (1) hoặc duy trì (0)

## Lưu ý phân tích

- Dữ liệu mất cân bằng nhãn, nên đánh giá thêm recall/F1/AUC bên cạnh accuracy.
- Names và Company thường là biến định danh, cần cân nhắc bỏ hoặc mã hóa cẩn thận để tránh overfitting.
- Nên tạo thêm feature từ Onboard_date (tháng, quý, năm onboarding).

## Bài toán phù hợp

- Dự đoán khách hàng rời bỏ (classification).
- Phân tích yếu tố ảnh hưởng đến churn theo nhóm khách hàng.
- Ước tính nhóm khách hàng cần ưu tiên trong chiến dịch giữ chân.
