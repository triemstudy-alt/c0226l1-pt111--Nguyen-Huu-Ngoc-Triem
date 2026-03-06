number = []
total = 0
for i in range(10):
    number.append(int(input("Nhập vào data trong list: ")))

for i in range(10):
    if number[i] > 10:
        total = total + number[i]
    else:
        continue

print(total)