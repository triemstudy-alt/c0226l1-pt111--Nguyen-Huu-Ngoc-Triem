subject = ["Toan", "Hoa", "Văn", "Lý", "Sử", "Địa", "Anh"]
score = {} #dùng dictionary để lưu lại kết quả sau khi 
for subject in (subject):
    score = (input(f"Nhập vào điểm của {subject} "))
    while score > 10 or score < 0:
        print("Sai format")
        score = int(input("Nhập lại điểm môn học: "))
    else:
        score[subject] = score
print(f"Điểm đã nhập của từng môn: ")
print(f"{subject}: {score}")
# Vẫn còn lỗi, fix sau