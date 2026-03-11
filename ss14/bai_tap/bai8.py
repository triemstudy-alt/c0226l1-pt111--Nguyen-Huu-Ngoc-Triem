t = (1, 2, 2, 3, 2, 4, 5)
for i in t:
    print(i, t.count(i))

def location():
    numb = int(input("Nhập vào số cần tìm: "))
    i = 0
    locate = 0
    for i in range(len(t)):       
        if t[i] == numb:
            locate = i+1
    print(f"Vị trí cuối cùng của số đã nhập: {locate}")

location()
