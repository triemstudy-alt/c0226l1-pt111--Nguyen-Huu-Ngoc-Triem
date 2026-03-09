friend= []

def showMenu():
    print("---------------Chương trình quản lý bạn bè trên Facebook--------------")
    print("Nhấn phím 1 để hiển thị danh sách bạn bè")
    print("Nhấn phím 2 để thêm mới bạn bè")
    print("Nhấn phím 3 để xóa bạn bè")
    print("Nhấn phím 4 để sửa tên bạn bè")
    print("Nhấn phím 5 để thoát chương trình")

def addFriend():
    name = input("Nhập tên bạn bè")
    friend.append(name)

def delFriend():
    name = input("Nhập tên bạn bè cần xóa: ")
    if name in friend:
        while name in friend:
            friend.remove(name)
        print("Đã xóa bạn:", name)
    else:
        print("Tên không có trong danh sách")


def updateFriend():
    name = input("Nhập tên bạn bè cần sửa: ")
    if name in friend:
        for i in range(len(friend)):
            if friend[i] == name:
                friend[i] = input("Nhập tên sau khi sửa: ")
                break
    else:
        print("Tên không có trong danh sách")

def showFriend():
    print(friend) 

