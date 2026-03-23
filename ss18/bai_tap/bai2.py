import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("Form Đăng ký Khuyến mãi")
root.geometry("500x350")
root.configure(bg="black")

title = tk.Label(
    root,
    text="ĐĂNG KÝ NHẬN KHUYẾN MÃI",
    fg="white",
    bg="black",
    font=("Arial", 14, "bold")
)
title.pack(pady=15)

frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

tk.Label(frame, text="Họ và tên:", fg="white", bg="black").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(frame, width=35)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Số điện thoại:", fg="white", bg="black").grid(row=1, column=0, sticky="w", pady=5)
phone_entry = tk.Entry(frame, width=35)
phone_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Email:", fg="white", bg="black").grid(row=2, column=0, sticky="w", pady=5)
email_entry = tk.Entry(frame, width=35)
email_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Ngày sinh:", fg="white", bg="black").grid(row=3, column=0, sticky="w", pady=5)

day_cb = ttk.Combobox(frame, width=5, values=[i for i in range(1, 32)])
day_cb.set("Ngày")
day_cb.grid(row=3, column=1, sticky="w")

month_cb = ttk.Combobox(frame, width=5, values=[i for i in range(1, 13)])
month_cb.set("Tháng")
month_cb.grid(row=3, column=1)

year_cb = ttk.Combobox(frame, width=7, values=[i for i in range(1900, 2027)])
year_cb.set("Năm")
year_cb.grid(row=3, column=1, sticky="e")

def submit():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    day = day_cb.get()
    month = month_cb.get()
    year = year_cb.get()
    with open ("khuyenmai.csv", "a") as f:
        f.write(f"Name: {name}, Phone: {phone}, Email: {email}, Day: {day}, Month: {month}, Year: {year}\n")

def clear():
    name = name_entry.delete(0, tk.END)
    phone = phone_entry.delete(0, tk.END)
    email = email_entry.delete(0, tk.END)
    day = day_cb.delete(0, tk.END)
    month = month_cb.delete(0, tk.END)
    year = year_cb.delete(0, tk.END)

def notice():
    mb.showinfo("Register data successfully")

def register():
    submit()
    clear()
    notice()
    
btn = tk.Button(
    root,
    text="Đăng ký nhận khuyến mãi",
    command=register,
    bg="gray",
    fg="white",
    width=25
)
btn.pack(pady=20)

root.mainloop()