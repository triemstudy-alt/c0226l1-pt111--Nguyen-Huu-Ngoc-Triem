import random
number = random.randint(1, 10)
count = 0
while count < 3:
    guest = int(input("Đoán 1 số ngẫu nhiên: "))
    if guest > number:
        print("Số bạn đoán đang lớn hơn")
        count += 1
    elif guest < number:
        print("Số bạn đoán đang nhỏ hơn")
        count += 1  
    elif guest == number:
        print("Congratulation!!")
        break
else:
    print("Đoán sai 3 lần rồi, end game")
