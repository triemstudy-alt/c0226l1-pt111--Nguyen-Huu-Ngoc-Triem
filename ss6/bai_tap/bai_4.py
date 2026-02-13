call_time = float(input("Nhập vào thời gian gọi: "))

if call_time <= 50 :
    print("Cước điện thoại: ", 25000+ call_time*600)
elif call_time >50 and call_time <= 200 :
    print("Cước điện thoại: ", 25000+ 50*600 + (call_time-50)*400)
elif call_time > 200:
    print("Cước điện thoại: ", 25000+ 50*600 + (call_time-50)*400 + (call_time- 200)*200)

    