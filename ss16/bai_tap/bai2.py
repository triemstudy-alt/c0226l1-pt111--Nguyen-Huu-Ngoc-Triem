import tkinter as tk

root = tk.Tk()
root.title("Login_Program")
root.geometry("400x300")

def lg():
    label = tk.Label(root,text ="Login")
    label.place(x=100, y=20)

def name():
    label = tk.Label(root, text="User name")
    label.place(x=100, y=50)
    entry = tk.Entry(root)
    entry.place(x=100, y=70)

def pw():
    label = tk.Label(root, text="Password")
    label.place(x=100, y = 100)
    entry = tk.Entry(root)
    entry.place(x=100,y = 120)

def btn():
    button = tk.Button(root, text="Login", command={})
    button.place(x= 100, y=150)

lg()
name()
pw()
btn()

root.mainloop() #Tạo tất cả các widget trước rồi mới chạy lệnh này
