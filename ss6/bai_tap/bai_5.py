a = int(input("Nhập vào số nguyên bất kỳ: "))

if a%3 == 0 and a%5 != 0 :
    print("Fizz")
elif a%5 == 0 and a%3 != 0:
    print("Buzz")
elif a%15 == 0 :
    print("Fizz- Buzz")