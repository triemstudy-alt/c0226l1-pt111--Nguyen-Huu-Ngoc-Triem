j = 1
for i in range(6):
    for j in (6,5,4,3,2,1):
        if j > i:
            print("*", end= " ")
        elif j == i:
            continue 
    print()    