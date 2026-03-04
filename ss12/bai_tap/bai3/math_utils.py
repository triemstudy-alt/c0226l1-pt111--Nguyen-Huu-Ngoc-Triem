def isEven(n):
    if n % 2 ==0:
        print(f"{n} là số chẵn")
    else:
        print(f"{n} không là số chẵn")

def isOdd(n):
    if n%2 != 0 :
        print(f"{n} là số lẻ")
    else:
        print(f"{n} không là số lẻ")


def isPrime(n):
    for i in range(1,n+1):
        count = 0
        if n/i == 1:
            count += 1
            if count == 2:
                print(f"{n} là số nguyên tố")
            else:
                print(f"{n} không là số nguyên tố")

            
