import random
number = random.randint(1, 100)
guest = int(input("Đoán 1 số ngẫu nhiên: "))
count = 1
while count < 7:
    while guest ==  number:
        print("Congratulation!!")
    guest = int(input("Sai rồi, đoán lại: "))
    count += 1
else:
    print("Đoán sai 7 lần rồi, end game")
