list = []
arrange = False
n = int(input("Nhập số lượng phần tử trong mảng: "))
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    list.append(value)

for j in range (n - 1):
    if list[j] <= list[j+1]:
        arrange = True
    else:
        arrange = False
        break
if arrange == True:
    print("OK")
else:
    print("NOK")
     