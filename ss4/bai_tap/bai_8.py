amount = float(input("Nhập vào số tiền gửi: "))
year = int(input("Nhập vào số năm: "))
rate = float(input("Nhập vào lãi suất: "))

print ("Tổng tiền lãi sau",year,"năm là: ", 
    str(amount*(1+rate/100)**year))

