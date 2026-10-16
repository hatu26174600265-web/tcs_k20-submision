# Bài 3: Giá trị, biến và kiểu dữ liệu
# Tác giả: Sinh viên KHDL

# 3.1. Khởi tạo một bản quan sát
ma_quan_sat = "OBS025"
so_lan_do = 4
gia_tri_do = 31.5
hop_le = True
ghi_chu = None

print("--- 3.1. Giá trị và kiểu dữ liệu của biến ---")
print(f"Giá trị: {ma_quan_sat}, Kiểu: {type(ma_quan_sat)}")
print(f"Giá trị: {so_lan_do}, Kiểu: {type(so_lan_do)}")
print(f"Giá trị: {gia_tri_do}, Kiểu: {type(gia_tri_do)}")
print(f"Giá trị: {hop_le}, Kiểu: {type(hop_le)}")
print(f"Giá trị: {ghi_chu}, Kiểu: {type(ghi_chu)}")

# 3.2. Gán lại giá trị
print("\n--- 3.2. Gán lại giá trị ---")
gia_tri_do = 31.5
print(gia_tri_do)

gia_tri_do = 29.8
print(gia_tri_do)
# Giải thích: Sau phép gán thứ hai, tên gia_tri_do truy cập giá trị mới là 29.8 
# (giá trị 31.5 trước đó đã bị ghi đè và thay thế hoàn toàn).

# 3.3. None và các giá trị khác
print("\n--- 3.3. So sánh None và các giá trị khác ---")
# Dự đoán kết quả: False, False, False
print(None == 0)      # Dự đoán: False
print(None == "")     # Dự đoán: False
print(None == False)  # Dự đoán: False
