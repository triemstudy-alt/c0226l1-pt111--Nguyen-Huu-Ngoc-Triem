income = float(input("Nhập vào tổng doanh số(đơn vị trăm triệu): "))

if income <= 100 :
    print("Hoa hồng nhận được: ", income/100*5)
elif income > 100 and income <= 300 :
    print("Hoa hồng nhận được: ", income/100*10)
elif income > 300 :
    print("Hoa hồng nhận được: ", income/100*20)

    
    