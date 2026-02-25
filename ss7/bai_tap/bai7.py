name = input("Nhập họ và tên: ")
count = 0
for i in name:
    if i == "n":
        count += 1
print("Tổng ký tự n: ", count)