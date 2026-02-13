year = int(input("Nhập vào năm: "))

if year%4 == 0 and year%100 != 0 :
    print("Năm nhuận")
elif year%100 == 0 and year%400 != 0:
    print("Không phải năm nhuận")
elif year%100 == 0 and year%400 == 0:
    print("Năm nhuận")
else :
    print("Không phải năm nhuận")

    