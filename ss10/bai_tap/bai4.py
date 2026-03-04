numb1 = int(input("Nhập vào số nguyên đầu: "))
numb2 = int(input("Nhập vào số nguyên tiếp theo: "))
count1 = 0
count2 = 0
i = 1
j = 1
while i < numb1:
    if numb1 % i == 0:
        count1 = count1 + i
    i += 1
while j < numb2:
    if numb2 % j == 0:
        count2 = count2 + j
    j += 1
if count1 == numb2 and count2 == numb1:
    print(f"{numb1} và {numb2} là cặp số hoàn hảo")
else:
    print(f"{numb1} và {numb2} không là cặp số hoàn hảo")