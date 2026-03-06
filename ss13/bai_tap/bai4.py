number = []
count = 0
for i in range(10):
    number.append(int(input("Nhập vào data trong list: ")))

for i in range(10):
    if number[i] > 5:
        count += 1
print(count)