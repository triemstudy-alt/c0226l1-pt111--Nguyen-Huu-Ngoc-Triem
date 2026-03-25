import math as m

def checkFraction():
    x = input("Nhập một số bất kỳ: ")
    if "/" not in x:
        return False   
    if x.count("/") == 1:
        try:
            xx, yy = x.split("/")     # 👈 phải split trước
            xx = int(xx)
            yy = int(yy)
            if yy == 0:
                return False
            gcd = m.gcd(xx, yy)
            reduced_xx = xx // gcd 
            reduced_yy = yy // gcd
            return f"{reduced_xx}/{reduced_yy}"
        except ValueError:
            return False
    return False
result = checkFraction()  

if result == False:
    print("Số bạn nhập không phải là phân số hợp lệ.")
else:
    print(f"Số đã rút gọn: {result}")