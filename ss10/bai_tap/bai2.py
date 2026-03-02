data = input("Nhập chuỗi bất kỳ: ")
count = 0
i = 0
x = 0
isPalindrome = True
for i in data:
    count += 1
for x in range((count+1)//2):
    if data[x] == data[-(x+1)]:
        isPalindrome = True
    else:
        isPalindrome = False
        break
if isPalindrome == True:
    print("Đây là dãy Palindrome")
else:
    print("Không phải dãy Palindrome")