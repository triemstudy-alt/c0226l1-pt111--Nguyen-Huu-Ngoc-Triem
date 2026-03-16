countries = {'Viet Nam':'Ha Noi', 'Indonesia':'Jakarta', 'USA':'Washington'}

def display():
    print("-----------Chương trình quản lý quốc gia và thủ đô---------------")
    print("Nhập phím 1 để hiển thị danh sách quốc gia và thủ đô")
    print("Nhập phím 2 để thêm mới quốc gia và thủ đô")
    print("Nhập phím 3 để xóa quốc gia và thủ đô")
    print("Nhập phím 4 để sửa tên thủ đô")
    print("Nhập phím 5 để tra cứu thủ đô")
    print("Nhập phím 6 để thoát chương trình")
    data = int(input())
    return data

def showData(data):
    if data == 1:
        print("Danh sách quốc gia và thủ đô tương ứng: ", countries)

def addData(data):
    if data == 2:
        data1 = input("Nhập vào tên quốc gia: ")
        data2 = input("Nhập vào tên thủ đô tương ứng: ")
        countries.update({data1:data2})
        print("Danh sách quốc gia và thủ đô mới: ", countries)

def delData(data):
    if data == 3:
        data3 = input("Nhập tên quốc gia cần xóa: ")
        for key, value in countries.copy().items():
            if key == data3:
                del countries[key]
        else:
            print("Tên quốc gia không tồn tại")
        print("Danh sách quốc gia và thủ đô mới: ", countries)



def updateData(data):
    if data == 4:
        data4 = input("Nhập vào tên quốc gia có thủ đô cần chỉnh sửa: ")
        if data4 in countries:
            data5 = input("Nhập vào tên thủ đô mới: ")
            countries[data4] = data5
            print("Danh sách quốc gia và thủ đô mới: ", countries)
        else:
            print("Tên quốc gia không tồn tại trong danh sách")

def findData(data):
    if data == 5:
        data6 = input("Nhập vào tên quốc gia muốn tìm kiếm: ")
        for key, value in countries.items():
            if data6 == key:
                print("Tên thủ đô tương ứng: ", countries.get(key))

    
