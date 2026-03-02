n = int(input("Nhập vào số n bất kỳ: "))
value1 = 0
value2 = 1
count = 0
while count < n and n > 0:
    print(value1, end=" ")
    value1, value2 = value2, value1+value2
    count += 1