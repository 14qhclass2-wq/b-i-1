# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))

tong = 0
i = 1

# Vòng lặp chạy khi i còn nhỏ hơn hoặc bằng n
while i <= n:
    tong += i  # Cộng dồn i vào tong
    i += 1     # Tăng biến đếm i lên 1

print(f"Tổng các số từ 1 đến {n} là: {tong}")