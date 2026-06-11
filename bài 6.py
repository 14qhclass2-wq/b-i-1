# Nhập số điện tiêu thụ
kwh = int(input("Nhập số điện tiêu thụ trong tháng (kWh): "))

# Xác định đơn giá theo quy tắc
if kwh <= 50:
    don_gia = 1800
elif kwh <= 100:
    don_gia = 2000
else:
    don_gia = 2500

# Tính tổng tiền
tong_tien = kwh * don_gia

# In kết quả
print("\n--- HÓA ĐƠN TIỀN ĐIỆN ---")
print(f"Số điện đã dùng: {kwh} kWh")
print(f"Đơn giá áp dụng: {don_gia:,} đồng/kWh")
print(f"Tổng tiền phải trả: {tong_tien:,} đồng") 