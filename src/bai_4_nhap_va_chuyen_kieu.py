# Bài 4: Nhập dữ liệu và chuyển đổi kiểu
# Tác giả: Sinh viên KHDL

# 4.1. Nhập ba trường dữ liệu và chuyển đổi kiểu
ma_quan_sat = input("Nhập mã quan sát: ")
so_lan_do = int(input("Nhập số lần đo (số nguyên): "))
gia_tri_do = float(input("Nhập giá trị đo (số thực - độ C): "))
don_vi = input("Nhập đơn vị đo: ")

# 4.2. Tính giá trị dẫn xuất và kiểm tra kiểu
gia_tri_f = gia_tri_do * 9 / 5 + 32

print("\n--- KẾT QUẢ QUAN SÁT ---")
print(f"Mã quan sát: {ma_quan_sat}")
print(f"Số lần đo: {so_lan_do} (Kiểu: {type(so_lan_do)})")
print(f"Giá trị đo: {gia_tri_do} {don_vi} (Kiểu: {type(gia_tri_do)})")
print(f"Giá trị chuyển sang độ F: {gia_tri_f:.2f} °F")

# Chuyển đổi ngược lại từ số sang chuỗi (str)
so_lan_do_text = str(so_lan_do)
print(f"Biến so_lan_do_text: '{so_lan_do_text}' có kiểu: {type(so_lan_do_text)}")
