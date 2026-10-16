# Bài 5: F-string, thời gian và chương trình tích hợp
# Tác giả: Sinh viên KHDL

from datetime import datetime

# 5.1. Thiết kế dữ liệu nhập
ma_quan_sat = input("Nhập mã quan sát: ")
ten_dai_luong = input("Nhập tên đại lượng: ")
gia_tri_do = float(input("Nhập giá trị đo (số thực): "))
don_vi = input("Nhập đơn vị: ")

# 5.2. Lấy thời điểm hiện tại thực tế từ hệ thống
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

# 5.3. Xuất bản ghi bằng f-string (Giá trị đo hiển thị chính xác 2 chữ số thập phân :.2f)
print("\n--- BẢN GHI QUAN SÁT ---")
print(f"Mã quan sát : {ma_quan_sat}")
print(f"Đại lượng   : {ten_dai_luong}")
print(f"Giá trị     : {gia_tri_do:.2f} {don_vi}")
print(f"Thời điểm   : {thoi_diem_text}")
