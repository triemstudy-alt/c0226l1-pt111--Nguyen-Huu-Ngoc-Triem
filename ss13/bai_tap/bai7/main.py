import function as fc

fc.showMenu()
select = int(input("Nhập vào yêu cầu: "))
if select == 1:
    fc.showFriend()
    fc.showMenu()
elif select == 2:
    fc.addFriend()
    fc.showMenu()
elif select == 3:
    fc.delFriend()
    fc.showMenu()
elif select == 4:
    fc.updateFriend()
    fc.showMenu()
elif select == 5:
    exit
else:
    print(input("Lệnh không khớp, vui lòng nhập lại: "))
