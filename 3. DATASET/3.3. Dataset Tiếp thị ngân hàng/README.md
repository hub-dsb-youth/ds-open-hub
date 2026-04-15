# 3.3. Dataset Tiếp thị ngân hàng

Nguồn gốc: Mô tả các thuộc tính của bộ dữ liệu Bank Marketing (Bản bổ sung).docx

## Mô tả dữ liệu

Bộ dữ liệu bank-additional-full là phiên bản mở rộng của Bank Marketing UCI, bổ sung bối cảnh kinh tế - xã hội để dự đoán kết quả chiến dịch telemarketing.

## Thông tin tệp dữ liệu

- Tệp dữ liệu: bank-additional-full.csv
- Số dòng: 41,188
- Số cột: 21 (20 biến đầu vào + 1 biến mục tiêu)
- Định dạng phân tách: dấu chấm phẩy (;)
- Biến mục tiêu: y (yes/no)
- Phân bố nhãn:
	- yes: 4,640 (~11.27%)
	- no: 36,548 (~88.73%)

## Nhóm biến chính

- Nhóm nhân khẩu học: age, job, marital, education
- Nhóm trạng thái tài chính: default, housing, loan
- Nhóm liên hệ chiến dịch: contact, month, day_of_week, duration, campaign, pdays, previous, poutcome
- Nhóm bối cảnh kinh tế vĩ mô: emp.var.rate, cons.price.idx, cons.conf.idx, euribor3m, nr.employed
- Nhãn dự đoán: y

## Lưu ý quan trọng khi mô hình hóa

- duration là biến dễ gây leakage, vì giá trị này chỉ biết sau khi cuộc gọi kết thúc. Nếu xây dựng mô hình dự đoán trước khi gọi, nên loại bỏ biến này.
- Giá trị 999 ở pdays thường được hiểu là chưa từng được liên hệ trước đó.
- Nhiều biến danh mục có giá trị unknown cần được xử lý nhất quán.
- Dữ liệu mất cân bằng nhãn, cần đánh giá thêm precision/recall/F1 thay vì chỉ dùng accuracy.

## Bài toán phù hợp

- Dự đoán thành công chiến dịch telemarketing.
- Phân tích tác động của chỉ số kinh tế vĩ mô đến hành vi đăng ký tiền gửi.
- So sánh hiệu năng mô hình trên dữ liệu mất cân bằng và dữ liệu có leakage/không leakage.

## Nguồn tham khảo

- Moro, S., Cortez, P., Rita, P. (2014). A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems.
