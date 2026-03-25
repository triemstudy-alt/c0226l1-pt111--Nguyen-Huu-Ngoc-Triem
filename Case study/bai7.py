list = []
check = 0
n = int(input("Nhập số lượng phần tử trong mảng: "))
for i in range(n):
    value = (input(f"Nhập phần tử thứ {i + 1}: "))
    list.append(value)
for j in range (n - 1):
    if list[j].isdigit() == True:
        check = check+1
    else:
        check = check+0
if check == 0:
    print("Mảng chỉ chứa ký tự")
elif check == n:
    print("Mảng chỉ chứa số")
else:
    print("Mảng hỗn hợp")