def read_file():
    try:
        with open("sample.csv", "r", encoding="utf-8") as f:
            data = f.read()
            return data
    except FileNotFoundError:
        print("Lỗi: File không tồn tại")