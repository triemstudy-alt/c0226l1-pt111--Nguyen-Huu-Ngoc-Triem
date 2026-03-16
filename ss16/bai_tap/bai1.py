import tkinter as tk

root = tk.Tk()
root.title("First_Program")
root.geometry("400x300")

#root.mainloop() #Tạo tất cả các widget trước rồi mới chạy lệnh này
def name():
    label = tk.Label(root, text="User name")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()

def pw():
    label = tk.Label(root, text="Password")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()

def btn():
    button = tk.Button(root, text="Login", command={})
    button.pack()

name()
pw()
btn()

root.mainloop() #Tạo tất cả các widget trước rồi mới chạy lệnh này
