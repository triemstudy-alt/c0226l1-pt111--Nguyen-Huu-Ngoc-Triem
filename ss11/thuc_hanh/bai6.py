numb = int(input("Nhập vào số nguyên bất kỳ: "))

def snt(numb):
   for i in range (1,numb+1):
         count = 0
         for j in range (1,i+1):
            if i % j == 0:
               count += 1
         if count == 2:
            print (i)
snt(numb)