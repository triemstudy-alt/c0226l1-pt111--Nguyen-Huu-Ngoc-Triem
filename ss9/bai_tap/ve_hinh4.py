rows = 8
cols = 20
for i in range(rows):
    if i == 0 or i == rows - 1:
        print("*" * cols)
    else:
        print("*" + " " * (cols - 2) + "*")