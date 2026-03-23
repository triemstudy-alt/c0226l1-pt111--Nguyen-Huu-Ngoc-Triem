import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("Chương trình tính toán")
root.geometry("500x350")
root.configure(bg="black")

title = tk.Label(
    root,
    text="NHẬP VÀO 2 SỐ NGUYÊN",
    fg="white",
    bg="black",
    font=("Arial", 14, "bold")
)
title.pack(pady=15)

frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

tk.Label(frame, text="Nhập vào số đầu: ", fg="white", bg="black").grid(row=0, column=0, sticky="w", pady=5)
first_entry = tk.Entry(frame, width=15)
first_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Nhập vào số sau:", fg="white", bg="black").grid(row=1, column=0, sticky="w", pady=5)
second_entry = tk.Entry(frame, width=15)
second_entry.grid(row=1, column=1, pady=5)

def cal():
    try:
        value1 = float(first_entry.get())
        value2 = float(second_entry.get())

        if value2 == 0:
            mb.showerror("Error", "Không thể chia cho 0")
            return

        result = value1 / value2

        mb.showinfo("Result", f"{value1} / {value2} = {result}")

    except ValueError:
        mb.showerror("Error", "Vui lòng nhập số hợp lệ")
    except ZeroDivisionError:
        mb.showerror("Error", "Không thể chia cho 0")

btn = tk.Button(root, text= "Chia hai số",command=cal, fg= "black", bg = "white", width= 20)
btn.pack()

root.mainloop()