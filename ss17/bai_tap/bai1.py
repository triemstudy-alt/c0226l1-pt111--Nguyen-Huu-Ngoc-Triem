import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("First_Program")
root.geometry("400x300")

label = tk.Label(root, text="Tên của bạn")
label.pack()
entryName = tk.Entry(root)
entryName.pack()

value = ""
def data(event):
    value = entryName.get()
    return value

def msg():
    mb.showinfo(f"Bạn đã đăng nhập bằng tên " + value)


button = tk.Button(root, text="Đăng nhập", command= msg)
button.pack()

#button.bind("<Button-1>",data)


root.mainloop() #Tạo tất cả các widget trước rồi mới chạy lệnh này
