import sympy
from sympy import isprime
list = []
count = 0
n = int(input("Nhập số lượng phần tử trong mảng: "))
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    list.append(value)
for j in list:
    if isprime(j) == True:
        count = count+1
    else:
        count = count+0
if count == n:
    print("Mảng chỉ chứa số nguyên tố")
else:
    print("Mảng hỗn hợp")
