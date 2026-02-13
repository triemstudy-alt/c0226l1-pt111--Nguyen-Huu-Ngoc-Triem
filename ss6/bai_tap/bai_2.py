a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
delta = b**2 - 4*a*c

if a == 0 and b == 0 :
    print("Phương trình vô nghiệm")
elif a == 0 and b != 0 :
    print("Nghiệm của phương trình: ", (-c/b))
elif delta < 0 :
    print("Phương trình vô nghiệm")
elif delta == 0 :
    print("Phương trình có nghiệm kép: ", -b/(2*a))
elif delta > 0 :
    print ("Phương trình có 2 nghiệm phân biệt là: "
    , (-b+ delta**0.5)/ (2*a) ,
    "và"
    , (-b- delta**0.5)/ (2*a))
    

    
    