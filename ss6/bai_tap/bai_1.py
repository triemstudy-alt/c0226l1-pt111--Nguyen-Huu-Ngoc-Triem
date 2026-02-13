gross = float(input("Nhập vào lương gross (xxTriệu): "))

if gross > 15 :
    print ("Lương thực nhận = ", (gross - (gross*30/100)))
elif gross > 7 and gross <= 15:
    print ("Lương thực nhận = ", (gross - (gross*20/100)))
elif gross < 7 :
    print ("Lương thực nhận = ", (gross - (gross*10/100)))
    
    