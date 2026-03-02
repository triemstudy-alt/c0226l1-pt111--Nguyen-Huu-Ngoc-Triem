subject = ["Toan", "Hoa", "Văn", "Lý", "Sử", "Địa", "Anh"]
score = 0
for subject in (subject):
    score = int(input(f"Nhập vào điểm của {subject} "))
    while score > 10 or score < 0:
        print("Sai format")
        score = int(input("Nhập lại điểm môn học: "))