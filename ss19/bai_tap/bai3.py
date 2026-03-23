import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("Quản lý danh sách sinh viên")
root.geometry("500x500")
root.configure(bg="black")

title = tk.Label(
    root,
    text="QUẢN LÝ SINH VIÊN",
    fg="white",
    bg="black",
    font=("Arial", 14, "bold")
)
title.pack(pady=15)

frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

tk.Label(frame, text="Tên sinh viên: ", fg="white", bg="black").grid(row=0, column=0, sticky="w", pady=5)
name = tk.Entry(frame, width=35)
name.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Tuổi:", fg="white", bg="black").grid(row=1, column=0, sticky="w", pady=5)
age = tk.Entry(frame, width=35)
age.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Lớp:", fg="white", bg="black").grid(row=2, column=0, sticky="w", pady=5)
sclass = tk.Entry(frame, width=35)
sclass.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Quê quán:", fg="white", bg="black").grid(row=3, column=0, sticky="w", pady=5)
location = tk.Entry(frame, width=35)
location.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Số điện thoại:", fg="white", bg="black").grid(row=4, column=0, sticky="w", pady=5)
phone = tk.Entry(frame, width=35)
phone.grid(row=4, column=1, pady=5)

def checkData():
    value1 = name.get()
    value2 = age.get()
    value3 = sclass.get()
    value4 = location.get()
    value5 = phone.get() 
    if not value1:
        mb.showwarning("Validation error","Tên không được để trống")
    if not value2:
        mb.showwarning("Validation error","Tuổi không được trống")
    try:
        value2 = float(age.get())
    except ValueError:
        mb.showerror("Data error","Sai định dạng tuổi")         

def updateData(): 
    value1 = name.get()
    value2 = age.get()
    value3 = sclass.get()
    value4 = location.get()
    value5 = phone.get()   
    with open ("danhsachsinhvien.csv", "a", encoding="utf-8") as f:
        f.write(f"Tên: {value1}, SDT: {value5}, Tuổi: {value2}, Lớp: {value3}, Quê quán: {value4}\n")

def clearData():
    value1 = name.delete(0, tk.END)
    value2 = age.delete(0, tk.END)
    value3 = sclass.delete(0, tk.END)
    value4 = location.delete(0, tk.END)
    value5 = phone.delete(0, tk.END)
    mb.showinfo("Success", "Đã lưu data vào file")  

def func():
    checkData()
    updateData()
    clearData()

btn = tk.Button(root, text= "Update infor",command=func, fg= "black", bg = "white", width= 20)
btn.pack()

root.mainloop()
