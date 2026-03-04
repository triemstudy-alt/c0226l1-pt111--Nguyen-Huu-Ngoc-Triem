import random
# password = str(random.randint(000,999))
password = f"{random.randint(0,999):03}"
a = 0
b = 0
c = 0
guess = "0"
print(f"Random password: {password}")

for a in range(10):
    for b in range(10):
        for c in range(10):
            guess = str(a)+ str(b)+ str(c)
            if guess == password:
                print(f"Password guess is : {guess}")
                break
            else:
                continue
        else:
            continue
        break
    else:
        continue
    break