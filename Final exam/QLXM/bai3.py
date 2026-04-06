import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
import pandas as pd

# tạo file nếu chưa có
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    f.write("Biển số xe,Họ tên sinh viên,Chứng minh nhân dân,Hãng xe máy,Phí gửi xe đã đóng\n")

brand_list = ["Yamaha", "Honda", "Suzuki", "Piaggio", "SYM", "Ducati", "Hãng khác"]

root = tk.Tk()
root.title("Quản lý gửi xe máy CodeGym")
root.geometry("1000x400")

# Treeview
tree = ttk.Treeview(root, columns=("plate", "name", "cmnd", "brand", "fee"), show="headings")
tree.heading("plate", text="Biển số xe")
tree.heading("name", text="Họ tên sinh viên")
tree.heading("cmnd", text="Chứng minh nhân dân")
tree.heading("brand", text="Hãng xe máy")
tree.heading("fee", text="Phí gửi xe đã đóng")

tree.pack()

# load data
df = pd.read_csv("data.csv")
for _, row in df.iterrows():
    tree.insert("", tk.END, values=list(row))

def validate_plate(plate):
    def is_duplicate_in_tree(plate):
        for item in tree.get_children():
            values = tree.item(item, "values")
            if values[0] == plate:
                return True
        return False

    if len(plate) == 0 or len(plate) > 20:
        return False
    df = pd.read_csv("data.csv")
    if plate in df["Biển số xe"].values:
        return False
    return True

def validate_cmnd(cmnd):
    if len(cmnd) == 0 or len(cmnd) > 16:
        return False
    if not cmnd.isdigit():
        return False
    return True

def validate_name(name):
    if len(name) == 0 or len(name) > 40:
        return False
    return True

def validate_fee(fee):
    if len(fee) == 0 or not fee.isdigit():
        return False
    return True

def add_vehicle():
    form = tk.Toplevel(root)

    tk.Label(form, text="Tên").grid(row=0, column=0)
    name_entry = tk.Entry(form)
    name_entry.grid(row=0, column=1)

    tk.Label(form, text="Biển số").grid(row=1, column=0)
    plate_entry = tk.Entry(form)
    plate_entry.grid(row=1, column=1)

    tk.Label(form, text="CMND").grid(row=2, column=0)
    cmnd_entry = tk.Entry(form)
    cmnd_entry.grid(row=2, column=1)

    tk.Label(form, text="Phí").grid(row=3, column=0)
    fee_entry = tk.Entry(form)
    fee_entry.grid(row=3, column=1)

    tk.Label(form, text="Hãng xe").grid(row=4, column=0)
    brand_cb = ttk.Combobox(form, values=brand_list)
    brand_cb.grid(row=4, column=1)

    def submit():
        name = name_entry.get()
        plate = plate_entry.get()
        cmnd = cmnd_entry.get()
        brand = brand_cb.get()
        fee = fee_entry.get()

        try:
            if not validate_name(name):
                raise ValueError("Tên không hợp lệ")
            if not validate_plate(plate):
                raise ValueError("Biển số đã tồn tại / sai")
            if not validate_cmnd(cmnd):
                raise ValueError("CMND sai")
            if not validate_fee(fee):
                raise ValueError("Phí sai")
        except ValueError as e:
            mb.showerror("Lỗi", str(e))
            return

        tree.insert("", tk.END, values=(plate, name, cmnd, brand, fee))

        with open("data.csv", "a", encoding="utf-8") as f:
            f.write(f"{plate},{name},{cmnd},{brand},{fee}\n")

        form.destroy()

    tk.Button(form, text="Submit", command=submit).grid(row=5, column=0)
    tk.Button(form, text="Cancel", command=form.destroy).grid(row=5, column=1)

def delete_vehicle():
    selected = tree.selection()
    confirm = mb.askyesno("Xác nhận", "Bạn có chắc muốn xóa không?")
    if confirm:
        for item in selected:
            tree.delete(item)

tk.Button(root, text="Thêm", command=add_vehicle).pack()
tk.Button(root, text="Xóa", command=delete_vehicle).pack()

root.mainloop()