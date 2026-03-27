import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox as mb
import csv

root = tk.Tk()
root.title("Quản lý học viên")
root.geometry("800x400")

def open_modal():
    modal = tk.Toplevel(root)
    modal.title("Nhập thông tin học viên")
    modal.geometry("350x300")

    # chặn window chính
    modal.grab_set()

    # ===== Input fields =====
    labels = ["Mã học viên", "Tên", "Lớp", "Email", "Ngày sinh"]
    entries = []

    for i, text in enumerate(labels):
        tk.Label(modal, text=text).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(modal)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    # ===== Submit =====
    def reload():
        tree.delete(*tree.get_children())
        with open("data.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                tree.insert("", "end", values=row)

    def submit():
        # Dùng strip() để loại bỏ khoảng trắng thừa
        ma = entries[0].get().strip()
        ten = entries[1].get().strip()
        lop = entries[2].get().strip()
        email = entries[3].get().strip()
        ngaysinh = entries[4].get().strip()
        # validate data
        if "" in [ma, ten, lop, email, ngaysinh]: # kiểm tra nếu có trường nào trống thì show error 
            mb.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return
        try:
            file_exists = os.path.isfile("data.csv")
            with open("data.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                if not file_exists: # nếu file chưa tồn tại thì viết header trước khi viết dữ liệu
                    header = ["Mã học viên", "Tên", "Lớp", "Email", "Ngày sinh"]
                    writer.writerow(header)
                writer.writerow([ma, ten, lop, email, ngaysinh]) # viết dữ liệu vào file
            mb.showinfo("Thành công", "Đã nhập dữ liệu!")
            modal.destroy() # đóng modal sau khi nhập xong
            reload() # reload lại dữ liệu trên treeview
        except Exception as e: # nếu có lỗi khi lưu file thì show error
            mb.showerror("Lỗi", f"Lỗi khi lưu file: {e}")
    # ===== Buttons =====
    tk.Button(modal, text="Lưu", command=submit).grid(row=6, column=0, pady=10)
    tk.Button(modal, text="Hủy", command=modal.destroy).grid(row=6, column=1)

# ====== Frame chứa button ======
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

btn_add = tk.Button(frame_btn, text="Thêm mới học viên", command=open_modal)
btn_add.grid(row=0, column=0, padx=5)

btn_edit = tk.Button(frame_btn, text="Sửa thông tin học viên")
btn_edit.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_btn, text="Xóa học viên")
btn_delete.grid(row=0, column=2, padx=5)

# ====== Table (Treeview) ======
columns = ("id", "name", "class", "email", "dob")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.pack(fill="both", expand=True)

# ====== Đặt tiêu đề ======
tree.heading("id", text="Mã học viên")
tree.heading("name", text="Tên")
tree.heading("class", text="Lớp")
tree.heading("email", text="Email")
tree.heading("dob", text="Ngày sinh")

# ====== Set width ======
tree.column("id", width=100)
tree.column("name", width=150)
tree.column("class", width=100)
tree.column("email", width=200)
tree.column("dob", width=100)

root.mainloop()