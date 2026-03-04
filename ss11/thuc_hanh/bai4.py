data = input("Nhập data cần check: ")

def check(data):
    for i in data:
        if i < "0" or i > "9":
            return False
    return True
isNumb = check(data)

if isNumb == True:
    print("Là chuỗi số")
else:
    print("Không là chuỗi số")
