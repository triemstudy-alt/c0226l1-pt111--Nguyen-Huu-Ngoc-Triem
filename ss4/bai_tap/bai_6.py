n = int(input("Nhập số nguyên 3 chữ số: "))

hang_don_vi = n % 10
hang_chuc = (n // 10) % 10
hang_tram = n // 100

tong = hang_tram + hang_chuc + hang_don_vi

print("Tổng các chữ số:", tong)
