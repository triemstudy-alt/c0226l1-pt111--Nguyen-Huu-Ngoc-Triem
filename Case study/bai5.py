def findMaxnumber():
    n = int(input("Nhập vào số bất kỳ: "))
    count = 0
    is_max = 0
    list = []
    result = 0
    for digit in n:
        if count(digit) < 5:
            return "-1"
        elif count(digit) > 5:
            digit.append(list)
    for i in list:
        result = int("".join(str(i) for i in list))