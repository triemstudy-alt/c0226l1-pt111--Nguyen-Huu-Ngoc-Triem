numbers = (2, 4, 6, 8, 10)
count = 0

for i in numbers:
    count = count + i
    print(count)

max = numbers[0]
for j in range(len(numbers)):
    if numbers[j] >= max:
        max = numbers[j]
print(max)

