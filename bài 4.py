
def input_list(n):
    danh_sach = []  #
    for i in range(n):
        phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
        danh_sach.append(phan_tu)  
    return danh_sach  


def count_negative(lst):
    dem_am = 0
    for num in lst:  
        if num < 0:
            dem_am += 1
    return dem_am

#######################

so_luong = int(input("Bạn muốn nhập bao nhiêu phần tử vào mảng? "))



my_list = input_list(so_luong)
print(f"Mảng bạn vừa nhập là: {my_list}")


so_luong_so_am = count_negative(my_list)


print(f"Số lượng phần tử âm trong mảng là: {so_luong_so_am}")