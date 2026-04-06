import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import csv
import re
from datetime import datetime

root = tk.Tk()
root.title("Quản lý học viên")
root.geometry("800x400")

# ====== Table (Treeview) ======
columns = ("id", "name", "class", "email", "dob")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.pack(fill="both", expand=True)
with open("data.csv", "r", encoding="utf-8") as f: #Show data as default when open app, đọc dữ liệu từ file CSV và hiển thị lên Treeview
            reader = csv.reader(f)
            next(reader) # bỏ qua dòng header
            for row in reader:
                tree.insert("", "end", values=row)

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

def is_duplicate_id(student_id, students):
    for s in students:
        if s["id"] == student_id:
            return True
    return False

def validate(student):
    # 1. ID: HV-XXXX
    if not re.match(r"^HV-\d{4}$", student["id"]): #dùng regex để kiểm tra định dạng ID, nếu không đúng thì show error
        mb.showerror("Error", "ID phải dạng HV-XXXX")
        return False
    if not student["id"].strip(): # kiểm tra nếu ID chỉ có khoảng trắng thì cũng không hợp lệ
        mb.showerror("Error", "ID không được để trống")
        return False

    # 2. Name <= 50 ký tự
    if len(student["name"]) > 50:
        mb.showerror("Error", "Tên tối đa 50 ký tự")
        return False

    # 3. Module: 1 -> 6
    if not student["module"].isdigit() or not (1 <= int(student["module"]) <= 6):
        mb.showerror("Error", "Module phải từ 1 đến 6")
        return False

    # 4. DOB: dd/mm/yyyy
    try:
        datetime.strptime(student["dob"], "%d/%m/%Y")
    except ValueError:
        mb.showerror("Error", "Ngày sinh phải dd/mm/yyyy")
        return False

    return True

def open_modal(): # hàm này sẽ được gọi khi người dùng click vào button "Thêm mới học viên"
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
        student = {"id": ma, "name": ten, "module": lop, "dob": ngaysinh} # tạo dict student để validate, module ở đây dùng để lưu lớp học
        valid, message = validate(student) # gọi hàm validate để kiểm tra dữ liệu, nếu không hợp lệ thì show error và return
        if not valid:
            mb.showerror("Error", message)
            return
        
        students = submit.read_students() # đọc danh sách học viên hiện có từ file CSV để kiểm tra trùng ID, submit.read_students() là một hàm tạm thời để đọc dữ liệu từ file CSV và trả về list các dict học viên
        students.append(student) # thêm student mới vào list students để kiểm tra trùng I

        if is_duplicate_id(student["id"], students):
            mb.showerror("Error", "ID đã tồn tại")
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

def edit_student():
    selected_item = tree.selection()
    if not selected_item:
        mb.showwarning("Lỗi", "Vui lòng chọn một học viên để sửa!")
        return
    # Lấy dữ liệu của học viên đã chọn
    item = tree.item(selected_item)
    values = item["values"]
    # Tạo modal để sửa thông tin
    modal = tk.Toplevel(root)
    modal.title("Sửa thông tin học viên")
    modal.geometry("350x300")
    modal.grab_set()

    labels = ["Mã học viên", "Tên", "Lớp", "Email", "Ngày sinh"]
    entries = []

    for i, text in enumerate(labels): 
# tạo các label và entry để hiển thị thông tin cũ và cho phép người dùng sửa,
# enumerate dùng để lặp qua labels và lấy index i để đặt vị trí row cho mỗi label và entry
        tk.Label(modal, text=text).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(modal)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, values[i]) # Điền sẵn dữ liệu cũ vào ô nhập
        entries.append(entry)

    def submit():
        if not validate():
            return
        ma = entries[0].get().strip()
        ten = entries[1].get().strip()
        lop = entries[2].get().strip()
        email = entries[3].get().strip()
        ngaysinh = entries[4].get().strip()
        if "" in [ma, ten, lop, email, ngaysinh]:
            mb.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return
        # Cập nhật dữ liệu trong treeview
        tree.item(selected_item, values=[ma, ten, lop, email, ngaysinh])
        # Cập nhật dữ liệu trong file CSV
        try:
            with open("data.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f) #biến reader để đọc dữ liệu từ file CSV, mỗi dòng là 1 list
                data = list(reader)
            for i in range(len(data)):
                if data[i][0] == values[0]: # Tìm dòng có mã học viên cũ để cập nhật
                    data[i] = [ma, ten, lop, email, ngaysinh] #mảng 2 chiều data
                    break
            with open("data.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            mb.showinfo("Thành công", "Đã cập nhật dữ liệu!")
            modal.destroy()
        except Exception as e:
            mb.showerror("Lỗi", f"Lỗi khi cập nhật file: {e}")

def delete_student():
    selected_item = tree.selection()
    if not selected_item:
        mb.showwarning("Lỗi", "Vui lòng chọn một học viên để xóa!")
        return
    item = tree.item(selected_item)
    values = item["values"]
    confirm = mb.askyesno("Xác nhận", f"Bạn có chắc muốn xóa học viên {values[1]}?") 
    # Hiển thị hộp thoại xác nhận với tên học viên để tránh xóa nhầm (askyesno trả về True nếu người dùng chọn "Yes" và False nếu chọn "No")
    if confirm:
        tree.delete(selected_item) # Xóa khỏi treeview
        # Xóa khỏi file CSV
        try:
            with open("data.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                data = list(reader)
            data = [row for row in data if row[0] != values[0]] # Giữ lại những dòng không có mã học viên cần xóa
            with open("data.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            mb.showinfo("Thành công", "Đã xóa học viên!")
        except Exception as e:
            mb.showerror("Lỗi", f"Lỗi khi cập nhật file: {e}")

frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

btn_add = tk.Button(frame_btn, text="Thêm mới học viên", command=open_modal)
btn_add.grid(row=0, column=0, padx=5)

btn_edit = tk.Button(frame_btn, text="Sửa thông tin học viên", command=edit_student)
btn_edit.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_btn, text="Xóa học viên", command=delete_student)
btn_delete.grid(row=0, column=2, padx=5)

root.mainloop()