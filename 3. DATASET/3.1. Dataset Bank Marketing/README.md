# 3.1. Dataset Bank Marketing

## Mô tả dữ liệu

Bộ dữ liệu mô tả chiến dịch tiếp thị qua điện thoại của một ngân hàng tại Bồ Đào Nha, dùng để dự đoán khả năng khách hàng đăng ký tiền gửi có kỳ hạn.

## Thông tin tệp dữ liệu

- Tệp dữ liệu: 3.1 Dataset Bank Marketing .csv
- Số dòng: 45,211
- Số cột: 17
- Định dạng phân tách: dấu chấm phẩy (;)
- Biến mục tiêu: y (yes/no)
- Phân bố nhãn:
	- yes: 5,289 (~11.70%)
	- no: 39,922 (~88.30%)

## Cấu trúc thuộc tính

- Nhóm nhân khẩu học: age, job, marital, education
- Nhóm tài chính/hồ sơ vay: default, balance, housing, loan
- Nhóm lịch sử liên hệ marketing: contact, day, month, duration, campaign, pdays, previous, poutcome
- Nhãn dự đoán: y

## Lưu ý phân tích

- Dữ liệu mất cân bằng nhãn (tỷ lệ yes thấp), nên cần cân nhắc stratified split, class_weight hoặc sampling.
- Các trường danh mục có nhiều giá trị unknown cần được xử lý rõ ràng (giữ nguyên, gom nhóm, hoặc imputation).
- Biến duration thường có độ quan trọng cao, nhưng có nguy cơ gây leakage trong một số tình huống dự đoán thực tế.

## Bài toán phù hợp

- Phân loại khách hàng có đăng ký tiền gửi hay không.
- Đánh giá hiệu quả chiến dịch telemarketing.
- Thực hành pipeline tiền xử lý dữ liệu hỗn hợp (số + danh mục).
