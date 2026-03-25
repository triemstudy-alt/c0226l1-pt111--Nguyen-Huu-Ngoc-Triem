def checkTriangle(a, b, c):
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    if a + b > c and a + c > b and b + c > a:
        return "Chỉ là 3 cạnh của tam giác"
    elif a <= 0 or b <= 0 or c <= 0:
        return "Không phải là tam giác"
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        return "Là 3 cạnh của tam giác vuông"
    elif a + b <= c or a + c <= b or b + c <= a:
        return "Không phải là tam giác"

checkTriangle()
