data = []
check = True
n = int(input("Nhập số lượng phần tử trong mảng: "))
for i in range(n): 
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    data.append(value)
for i in range(n-1):
    if data[i] > data[i+1]:
        check = False
        break
    else:
        check = True
if check == True:
    print("OK")
else:
    print("NOK")