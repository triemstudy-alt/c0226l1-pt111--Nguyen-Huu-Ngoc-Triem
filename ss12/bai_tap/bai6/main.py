import password_utils as pa
pw = input("Nhập password: ")

while pa.is_long_enough(pw) == False :
    pw = input("Không đủ điều kiện, nhập lại password: ")

if pa.is_strong_password(pw) == True: 
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")


