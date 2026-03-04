pi = 3.14
s = 0
c = 0
r = float(input("Nhập vào bán kính hình tròn: "))

def dien_tich(pi,r):
    return pi*(r*r)
def chu_vi(pi,r):
    return 2*pi*r

print(f"Diện tích hình tròn: {dien_tich(pi,r)}")
print(f"Chu vi hình tròn: {chu_vi(pi,r)}")