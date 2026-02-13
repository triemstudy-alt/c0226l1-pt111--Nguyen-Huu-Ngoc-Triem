# age = int(input("Nhập độ tuổi: "))
weight = float(input("Nhập cân nặng: "))
height = float(input("Nhập chiều cao: "))
bmi = weight/(height**2)

if bmi < 18.5 :
    print("Underweight")
elif bmi < 25 and bmi >= 18.5 :
    print("Normal")
elif bmi >= 25 and bmi < 30 :
    print("Overweight")
elif bmi >= 30 :
    print("Obese")

    
    
    