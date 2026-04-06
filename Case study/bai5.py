from itertools import combinations

def findMaxnumber():
    n = input("Nhập vào số bất kỳ: ")

    # tạo tất cả tổ hợp 3 chữ số
    combs = combinations(n, 3)

    # chuyển thành số
    numbers = [int("".join(c)) for c in combs]

    # nếu không đủ 3 chữ số
    if not numbers:
        return -1

    return max(numbers)


print(f"Value max: {findMaxnumber()}")