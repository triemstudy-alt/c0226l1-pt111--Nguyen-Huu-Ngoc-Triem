import csv
import os

FILE_NAME = "data.csv"


def read_students():
    students.append({
    "id": row["Mã học viên"],
    "name": row["Tên"],
    "module": row["Lớp"],
    "email": row["Email"],
    "dob": row["Ngày sinh"]
})
    students = []
    if not os.path.exists(FILE_NAME):
        return students

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append(row)
    return students

def write_students(students):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "name", "module", "email", "dob"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def add_student(student):
    students = read_students()
    students.append(student)
    write_students(students)

def update_student(old_id, new_student):
    students = read_students()
    for i, s in enumerate(students):
        if s["id"] == old_id:
            students[i] = new_student
            break
    write_students(students)

def delete_student(student_id):
    students = read_students()
    students = [s for s in students if s["id"] != student_id]
    write_students(students)