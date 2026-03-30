import re
from datetime import datetime

def validate(student):
    if not re.match(r"^HV-\d{4}$", student["id"]):
        return False, "ID phải dạng HV-XXXX"

    if not student["id"].strip():
        return False, "ID không được để trống"

    if len(student["name"]) > 50:
        return False, "Tên tối đa 50 ký tự"

    if not student["module"].isdigit() or not (1 <= int(student["module"]) <= 6):
        return False, "Module phải từ 1 đến 6"

    try:
        datetime.strptime(student["dob"], "%d/%m/%Y")
    except ValueError:
        return False, "Ngày sinh phải dd/mm/yyyy"

    return True, ""

def is_duplicate_id(student_id, students):
    return any(s["id"] == student_id for s in students)