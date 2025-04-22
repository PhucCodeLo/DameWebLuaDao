from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# ✅ DỮ LIỆU MỞ RỘNG
ho = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Đặng", "Bùi", "Đỗ", "Ngô", "Dương", "Tô", "Tạ", "Chu", "Lý", "Vũ", "Võ", "Kiều", "La", "Thái", "Đinh", "Cao", "Lương"]
dem = ["Văn", "Thị", "Minh", "Ngọc", "Thanh", "Hữu", "Trọng", "Phương", "Quốc", "Thùy", "Mai", "Khánh", "Nhật", "Xuân", "Tường", "Gia", "Trúc", "Diệu"]
ten = ["An", "Bình", "Cúc", "Dũng", "Hòa", "Lan", "Long", "Mai", "Nam", "Oanh", "Phúc", "Quân", "Sơn", "Trang", "Vinh", "Tuấn", "Linh", "Khoa", "Việt", "Hiếu", "Tâm", "Tú", "Duy", "Nga", "Nhung", "Lộc", "Thảo", "Vy", "Ngân", "Yến", "Thư", "Tuyết", "Châu", "Hạnh", "Thành", "Huy", "Khanh", "Tín", "Loan", "Hương", "Thiện", "Giang"]

# Số điện thoại thực tế Việt Nam (theo đầu số)
dau_so = ['096', '097', '098', '032', '033', '034', '035', '036', '037', '038', '039',  # Viettel
          '091', '094', '083', '084', '085',                                           # Vinaphone
          '090', '093', '070', '079', '077',                                           # Mobifone
          '092', '056', '058']                                                        # Vietnamobile, Wintel

# Tên đường + Quận + Tỉnh thật
duong = ["Nguyễn Huệ", "Trần Hưng Đạo", "Lý Thường Kiệt", "Nguyễn Văn Linh", "Phan Đình Phùng", "Cách Mạng Tháng 8", "Trần Phú", "Lê Lợi", "Hai Bà Trưng", "Pasteur", "Điện Biên Phủ"]
phuong = ["Phường 1", "Phường 2", "Phường 3", "Phường 5", "Phường Linh Trung", "Phường Thảo Điền", "Phường Bến Nghé", "Phường Hòa Minh"]
quan = ["Quận 1", "Quận 3", "Quận 5", "Quận 7", "TP. Thủ Đức", "Quận Hải Châu", "Quận Hoàn Kiếm", "TP. Huế", "TP. Biên Hòa", "Huyện Bình Chánh"]
tinh = ["TP.HCM", "Hà Nội", "Đà Nẵng", "Huế", "Bình Dương", "Đồng Nai", "Nghệ An", "Cần Thơ", "Bắc Ninh"]

# Sản phẩm & số lượng như yêu cầu
san_pham_list = [
    "Lelabo Santal 33",
    "Lelabo Another 13",
    "Lelabo Rose 31",
    "LeLabo The Noir 29",
    "Bleu Chanel EDP",
    "Dior Sauvage"
]

so_luong_options = [
    "Mua 1 chai: 549.000đ + 30k ship",
    "Mua 2 chai: 980.000đ + Miễn ship",
    "Mua 3 chai: 1.449.000đ + Miễn ship",
    "Mua 4 chai: 1.840.000đ + Miễn ship"
]

# ✅ Danh sách đã dùng để tránh trùng
used_combos = set()

def tao_ten_ngau_nhien():
    return f"{random.choice(ho)} {random.choice(dem)} {random.choice(ten)}"

def tao_sdt_ngau_nhien():
    return random.choice(dau_so) + ''.join(random.choices("0123456789", k=7))

def tao_dia_chi_ngau_nhien():
    so = random.randint(1, 300)
    return f"{so} {random.choice(duong)}, {random.choice(phuong)}, {random.choice(quan)}, {random.choice(tinh)}"

def get_unique_combo():
    while True:
        name = tao_ten_ngau_nhien()
        sdt = tao_sdt_ngau_nhien()
        diachi = tao_dia_chi_ngau_nhien()
        key = f"{name}|{sdt}|{diachi}"
        if key not in used_combos:
            used_combos.add(key)
            return name, sdt, diachi

# ✅ Gửi đơn
def submit_form(ten, sdt, dia_chi, san_pham, so_luong):
    service = Service("D:/chromedriver-win64/chromedriver.exe")  # Đường dẫn driver của anh
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.bluxuryperfume.org/lelabo")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "name")))

        driver.find_element(By.NAME, "name").send_keys(ten)
        driver.find_element(By.NAME, "phone").send_keys(sdt)
        driver.find_element(By.NAME, "address").send_keys(dia_chi)

        xpath_checkbox = f"//input[@type='checkbox' and @value='{san_pham}']"
        driver.find_element(By.XPATH, xpath_checkbox).click()

        dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select")))
        Select(dropdown).select_by_visible_text(so_luong)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='ĐẶT NGAY']"))
        )
        submit_button.click()

        print(f"✅ {ten} | {sdt} | {dia_chi} | {san_pham} | {so_luong}")
        time.sleep(5)

    except Exception as e:
        print(f"❌ Gặp lỗi: {e}")

    finally:
        driver.quit()

# ✅ Auto lặp
luot = 1
while True:
    ten, sdt, dia_chi = get_unique_combo()
    san_pham = random.choice(san_pham_list)
    so_luong = random.choice(so_luong_options)

    print(f"\n🔁 Đơn {luot}: {ten} | {sdt} | {san_pham} | {so_luong}")
    submit_form(ten, sdt, dia_chi, san_pham, so_luong)
    luot += 1
    time.sleep(3)  # nghỉ 30s trước khi gửi đơn mới
