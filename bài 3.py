def is_even(n):
    return n % 2 == 0
    

so_can_kiem_tra = int(input("Nhập một số cần kiểm tra chẵn lẻ: "))


if is_even(so_can_kiem_tra):
    print(f"{so_can_kiem_tra} là số CHẴN.")
else:
    print(f"{so_can_kiem_tra} là số LẺ.")