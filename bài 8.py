n = int(input("Nhập một số nguyên dương n: "))
giai_thua = 1
for i in range(1, n + 1):
    giai_thua = giai_thua * i  # Hoặc viết gọn là giai_thua *= i
print(f"Giai thừa của {n} là: {giai_thua}")