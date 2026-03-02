numb = int(input("Nhập vào số nguyên bất kỳ: "))
count = 1
i = 1
for i in range(1,numb+1):
    count = count*i 
print(f"Giai thừa của số đã nhập: {count}")
