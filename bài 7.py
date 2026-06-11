# Nhập số nguyên n
n = int(input("Nhập một số nguyên n cần kiểm tra: "))

print("\n--- KẾT QUẢ KIỂM TRA ---")

# 1. Kiểm tra chẵn / lẻ
if n % 2 == 0:
    print(f"+ {n} là số chẵn.")
else:
    print(f"+ {n} là số lẻ.")

# 2. Kiểm tra chia hết cho 3
if n % 3 == 0:
    print(f"+ {n} chia hết cho 3.")
else:
    print(f"+ {n} không chia hết cho 3.")

# 3. Kiểm tra chia hết cho cả 2 và 3
if n % 2 == 0 and n % 3 == 0:
    print(f"+ {n} chia hết cho cả 2 và 3 (chia hết cho 6).")
else:
    print(f"+ {n} không chia hết cho đồng thời cả 2 và 3.")