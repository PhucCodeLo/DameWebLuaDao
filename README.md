# 🧠 Auto Form Submission Tool - LeLabo Perfume Website

## 📌 Mục Đích
Tự động điền và gửi biểu mẫu đặt hàng trên trang [https://www.bluxuryperfume.org/lelabo](https://www.bluxuryperfume.org/lelabo), với thông tin hoàn toàn ngẫu nhiên: họ tên, số điện thoại, địa chỉ, sản phẩm và số lượng.

## ✅ Tính Năng
- Random tên thật (nam/nữ, cổ điển & hiện đại)
- Random số điện thoại hợp lệ của Viettel, Vina, Mobi, Vietnamobile
- Random địa chỉ chi tiết theo cấu trúc: số nhà, đường, phường, quận, tỉnh
- Random sản phẩm và số lượng từ danh sách có thật
- Tránh trùng lặp tên + SĐT + địa chỉ giữa các đơn
- Chạy liên tục và tự động mỗi 30 giây

---

## ⚙️ Hướng Dẫn Cài Đặt

### 1. Cài Đặt Python
- Tải Python 3.10 trở lên: https://www.python.org/
- Cài đặt và nhớ tick chọn "Add to PATH"

### 2. Cài Gói Phụ Thuộc
```bash
pip install selenium
```

### 3. Cài ChromeDriver
- Truy cập: https://googlechromelabs.github.io/chrome-for-testing/
- Tải phiên bản phù hợp với Chrome anh đang dùng
- Giải nén, lấy file `chromedriver.exe` và đặt vào thư mục, ví dụ: `D:/chromedriver-win64/chromedriver.exe`

---

## 🚀 Cách Sử Dụng

### 1. Tạo File Code
- Tạo file `auto_form_lelabo.py`
- Dán toàn bộ đoạn code Python đã được cung cấp

### 2. Cấu Hình Đường Dẫn ChromeDriver
```python
service = Service("D:/chromedriver-win64/chromedriver.exe")
```

### 3. Chạy Tool
```bash
python auto_form_lelabo.py
```

Tool sẽ tự động gửi đơn hàng mỗi 30 giây, với dữ liệu hoàn toàn mới.

---

## 🧪 Kết Quả Mẫu
```bash
🔁 Đơn 3: Đặng Hữu Quân | 0974929383 | 182 Nguyễn Văn Linh, Phường Linh Trung, Quận 1, TP.HCM | Dior Sauvage | Mua 2 chai: 980.000đ + Miễn ship
✅ Gửi thành công!
```

---

## 🔧 Gợi Ý Nâng Cấp
- Gửi ngẫu nhiên trong khung giờ (ví dụ 9h-17h)
- Giao diện có nút Bắt đầu/Dừng
- Xuất lịch sử gửi ra file CSV
- Tự động dừng sau 100 đơn

---

## 🛑 Dừng Tool
- Bấm `Ctrl + C` trong terminal để dừng thủ công

---

## 📂 Gợi Ý Tổ Chức Thư Mục
```
AutoFormLeLabo/
├── chromedriver.exe
├── auto_form_lelabo.py
├── README.md
```

---

## 📞 Liên Hệ / Hỗ Trợ
Nếu cần hỗ trợ nâng cấp thêm, vui lòng liên hệ đội dev nội bộ hoặc thông báo lại để được chỉnh sửa theo yêu cầu mới.

---

Chúc anh dùng tool hiệu quả!

