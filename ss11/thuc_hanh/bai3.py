numb = int(input("Nhập vào số nguyên bất kỳ: "))

def giai_thua(numb):
    total = 1
    i = 1
    while i < numb+1:
        total = total*i
        i += 1
    return total    
print(giai_thua(numb))
