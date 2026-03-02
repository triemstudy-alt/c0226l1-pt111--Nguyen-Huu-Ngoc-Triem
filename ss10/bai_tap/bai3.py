numb = int(input("Nhập vào số nguyên bất kỳ: "))
total = 0
for i in range(1,numb):
    if numb % i == 0:
        total = total + i 
if total == numb:
    print("Số hoàn hảo")
else:
    print("Không là số hoàn hảo")
    print(total)
