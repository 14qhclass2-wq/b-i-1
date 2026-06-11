dem = 0
tong = 0
while True:
    so = int(input("Nhập một số nguyên (nhập 0 để dừng): "))
    
    if so == 0:
        break  
        
    dem = dem + 1     
    tong = tong + so   

print(f"Số lượng số khác 0 đã nhập: {dem}")
print(f"Tổng các số đã nhập: {tong}")