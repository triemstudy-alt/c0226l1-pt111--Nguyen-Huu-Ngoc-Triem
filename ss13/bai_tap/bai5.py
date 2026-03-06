number = []
count = 0
for i in range(10):
    number.append(int(input("Nhập vào data trong list: ")))

n = int(input("Nhập vào n: "))
number.remove(n)
for i in range(len(number)):
    if number[i] > 5:
        count += 1
print(count)