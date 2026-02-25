name = input("Nhập họ và tên: ")
count = 0
check = input("Nhập vào ký tự cần kiểm tra: ")
for i in name:
    if i == check:
        count += 1
if count > 0 :
    print(check + " có tồn tại")
else:
    print(check + " không tồn tại")