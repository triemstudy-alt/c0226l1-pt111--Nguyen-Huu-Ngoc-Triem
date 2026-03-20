userData = []
def inputData():
    for i in range (1,6):
        name = input(f"Nhập vào tên user{i}: ")
        age = input(f"Nhập vào tuổi user{i}: ")
        location = input(f"Nhập vào quê quán user{i}: ")
        data = [name, age, location]
        userData.append(data)
    with open ("data.csv", "r+") as f:
        f.read()
        f.write(f"{userData}\n")

inputData()
print(userData)
