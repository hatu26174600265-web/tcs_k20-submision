# Bài 2: Toán tử và Biểu thức
# Tác giả: Sinh viên KHDL

# 2.1. Toán tử số học
a = 17
b = 5

print("--- 2.1. Toán tử số học ---")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

# Kiểm tra kiểu dữ liệu của kết quả a / b và a // b bằng type()
print(f"Kiểu dữ liệu của a / b ({a / b}) là: {type(a / b)}")
print(f"Kiểu dữ liệu của a // b ({a // b}) là: {type(a // b)}")

# 2.2. Bài toán chia nhóm
so_sinh_vien = 47
so_sv_moi_nhom = 5

so_nhom_du = so_sinh_vien // so_sv_moi_nhom
so_sv_con_lai = so_sinh_vien % so_sv_moi_nhom

print("\n--- 2.2. Bài toán chia nhóm ---")
print(f"Số nhóm đủ là: {so_nhom_du}")
print(f"Số sinh viên còn lại là: {so_sv_con_lai}")

# 2.3. Toán tử so sánh
gia_tri_do = 28.6
nguong = 30

print("\n--- 2.3. Toán tử so sánh ---")
print(f"gia_tri_do > nguong: {gia_tri_do > nguong}")
print(f"gia_tri_do < nguong: {gia_tri_do < nguong}")
print(f"gia_tri_do >= 28.6: {gia_tri_do >= 28.6}")
print(f"gia_tri_do <= 28: {gia_tri_do <= 28}")
print(f"gia_tri_do == 28.6: {gia_tri_do == 28.6}")
print(f"gia_tri_do != 30: {gia_tri_do != 30}")
