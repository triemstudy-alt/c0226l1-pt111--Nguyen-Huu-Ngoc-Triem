list = []
isTrue = 0
n = int(input("Nhập số lượng phần tử trong mảng: "))
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    list.append(value)
for j in list:
    if j%2 == 0:
        isTrue = isTrue+1
    else:
        isTrue = isTrue+0
if isTrue == n:
        print("Mảng chẵn")
elif isTrue == 0:
        print("Mảng lẻ")
elif isTrue > 0 and isTrue < n:
        print("Mảng hỗn hợp")
