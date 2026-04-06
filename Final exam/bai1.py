numb = []
validate = False
n = int(input("Nhập số lượng phần tử trong mảng: "))

for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    numb.append(value)
print(numb)

for i in range (1,len(numb)-1):
    if numb[i] > numb[i-1] and numb[i] > numb[i+1]:
        validate = True
    elif numb[i] < numb[i-1] and numb[i] < numb[i+1]:
        validate = True
    else:
        validate = False
        break

if validate == True:
    print("True")
else:
    print("False")  
