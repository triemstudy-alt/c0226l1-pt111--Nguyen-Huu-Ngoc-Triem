list = []
n = int(input("Nhập số lượng phần tử trong mảng: "))
for i in range(n):
    list.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
for i in range(n//2):
    if list[i] == list[-i-1]:
        print("Là mảng đối xứng")
        break
else:
    print("Không là mảng đối xứng")