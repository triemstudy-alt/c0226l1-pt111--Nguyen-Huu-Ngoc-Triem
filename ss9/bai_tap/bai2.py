numb = int(input("Nhập vào số nguyên bất kỳ: "))
i = 1
count = 0
for i in range(1,numb+1): 
    if numb%i == 0:
        count += 1
        while count == 2:
            print("Đây là số nguyên tố")
            break
        else:
            print("Đây không là số nguyên tố")
            break