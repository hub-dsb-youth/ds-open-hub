# 3.2. Dataset Online Retail

## Mô tả dữ liệu

Bộ dữ liệu giao dịch bán lẻ trực tuyến tại Anh, thường được dùng cho phân tích hành vi mua hàng và phân khúc khách hàng.

## Thông tin dữ liệu tổng quan

- Quy mô mô tả: 541,909 giao dịch
- Số cột: 8
- Mục tiêu sử dụng: phân tích doanh thu, RFM, phân cụm khách hàng, và phát hiện giao dịch bất thường

## Data Dictionary (8 cột phổ biến)

- InvoiceNo: mã hóa đơn
- StockCode: mã sản phẩm
- Description: mô tả sản phẩm
- Quantity: số lượng mua (có thể âm khi trả hàng)
- InvoiceDate: thời điểm giao dịch
- UnitPrice: đơn giá mỗi sản phẩm
- CustomerID: mã khách hàng
- Country: quốc gia

## Lưu ý chất lượng dữ liệu

- Quantity âm thường là giao dịch trả hàng/cancel.
- Đơn giá bằng 0 cần được xử lý riêng trước khi tính doanh thu.
- CustomerID có thể thiếu ở một phần giao dịch.
- Cần chuẩn hóa timezone và kiểu dữ liệu datetime trước khi tạo feature theo thời gian.

## Bài toán phù hợp

- Phân tích doanh thu theo thời gian, quốc gia, nhóm sản phẩm.
- RFM scoring và phân cụm khách hàng (K-Means/Hierarchical).
- Market basket và sản phẩm thường mua cùng nhau.

## Ghi chú

README này mô tả theo tài liệu gốc .docx. Nếu bộ CSV được bổ sung vào thư mục này, nên cập nhật thêm thống kê thực tế (số dòng sau làm sạch, tỷ lệ missing, và phân bố trả hàng).
