numb = int(input("Nhập số nguyên bất kỳ: "))

def total(numb):
   count = 0
   i = 1
   for i in range(0,numb+1,2):
      if i% 2 == 0:
         count += i
   print(count)
total(numb)