import tkinter as tk

value1 = ""
value2 = ""

root = tk.Tk()
root.title("Login_Program")
root.geometry("400x300")

label = tk.Label(root,text ="Login")
label.place(x=100, y=20)

label = tk.Label(root, text="User name")
label.place(x=100, y=50)
entry1 = tk.Entry(root)
entry1.place(x=100, y=70)

label = tk.Label(root, text="Password")
label.place(x=100, y = 100)
entry2 = tk.Entry(root)
entry2.place(x=100,y = 120)

def checkData(event = None):
    value1 = entry1.get()
    value2 = entry2.get()
    if value1 == "admin" and value2 == "123456":
        print("Đăng nhập thành công")
    else:
        print("Đăng nhập thất bại")
    print(value1, value2)

button = tk.Button(root, text="Login", command=checkData)
button.place(x= 100, y=150)

root.mainloop() 