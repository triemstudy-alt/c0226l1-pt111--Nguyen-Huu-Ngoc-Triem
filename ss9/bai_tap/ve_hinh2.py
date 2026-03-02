j = 1
for i in range(6):
    for j in range(6):
        if j < i:
            print("*", end= " ")
        elif j == i:
            continue 
    print()    