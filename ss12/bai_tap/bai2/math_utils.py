def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a != 0 and b != 0:
        return a/b
    else:
        print("Yêu cầu nhập lại số khác 0: ")
        a = float(input("Nhập lại số a: "))
        b = float(input("Nhập lại số b: "))
