import tkinter as tk
from tkinter import ttk, messagebox as mb

from manage_data import read_students, add_student, update_student, delete_student
from validate import validate, is_duplicate_id


def run_app():
    root = tk.Tk()
    root.title("Quản lý học viên")
    root.geometry("800x400")

    # ====== Table ======
    columns = ("id", "name", "module", "email", "dob")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.pack(fill="both", expand=True)

    headings = ["Mã học viên", "Tên", "Lớp", "Email", "Ngày sinh"]

    for col, text in zip(columns, headings):
        tree.heading(col, text=text)
        tree.column(col, width=150)

    # ====== Reload ======
    def reload():
        tree.delete(*tree.get_children())
        for s in read_students():
            tree.insert("", "end", values=(
                s["id"], s["name"], s["module"], s["email"], s["dob"]
            ))

    reload()

    # ====== Modal Form ======
    def open_modal(mode="add", selected=None):
        modal = tk.Toplevel(root)
        modal.title("Thông tin học viên")
        modal.geometry("350x300")
        modal.grab_set()

        labels = ["Mã học viên", "Tên", "Lớp", "Email", "Ngày sinh"]
        entries = []

        for i, text in enumerate(labels):
            tk.Label(modal, text=text).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(modal)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)

        # Nếu edit → fill data
        if mode == "edit" and selected:
            for i, value in enumerate(selected):
                entries[i].insert(0, value)

        def submit():
            student = {
                "id": entries[0].get().strip(),
                "name": entries[1].get().strip(),
                "module": entries[2].get().strip(),
                "email": entries[3].get().strip(),
                "dob": entries[4].get().strip()
            }

            valid, msg = validate(student)
            if not valid:
                mb.showerror("Error", msg)
                return

            students = read_students()

            # ===== ADD =====
            if mode == "add":
                if is_duplicate_id(student["id"], students):
                    mb.showerror("Error", "ID đã tồn tại")
                    return

                add_student(student)
                mb.showinfo("Thành công", "Đã thêm học viên!")

            # ===== EDIT =====
            elif mode == "edit":
                old_id = selected[0]

                if student["id"] != old_id and is_duplicate_id(student["id"], students):
                    mb.showerror("Error", "ID đã tồn tại")
                    return

                update_student(old_id, student)
                mb.showinfo("Thành công", "Đã cập nhật!")

            modal.destroy()
            reload()

        tk.Button(modal, text="Lưu", command=submit).grid(row=6, column=0, pady=10)
        tk.Button(modal, text="Hủy", command=modal.destroy).grid(row=6, column=1)

    # ====== Buttons ======
    frame = tk.Frame(root)
    frame.pack(pady=10)

    def handle_add():
        open_modal("add")

    def handle_edit():
        selected_item = tree.selection()
        if not selected_item:
            mb.showwarning("Lỗi", "Chọn học viên để sửa")
            return

        values = tree.item(selected_item)["values"]
        open_modal("edit", values)

    def handle_delete():
        selected_item = tree.selection()
        if not selected_item:
            mb.showwarning("Lỗi", "Chọn học viên để xóa")
            return

        values = tree.item(selected_item)["values"]

        confirm = mb.askyesno("Xác nhận", f"Xóa học viên {values[1]}?")
        if not confirm:
            return

        delete_student(values[0])
        mb.showinfo("Thành công", "Đã xóa!")
        reload()

    tk.Button(frame, text="Thêm", command=handle_add).grid(row=0, column=0, padx=5)
    tk.Button(frame, text="Sửa", command=handle_edit).grid(row=0, column=1, padx=5)
    tk.Button(frame, text="Xóa", command=handle_delete).grid(row=0, column=2, padx=5)

    root.mainloop()