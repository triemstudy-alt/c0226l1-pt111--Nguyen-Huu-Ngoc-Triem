date = input("Nhập chuỗi theo định dạng (dd/mm/yyyy): ")

def checkFormat(date):
    if len(date) != 10:
        return False
    if "/" not in date:
        return False
    return True

def checkYear(year):
    if checkFormat(date) == True and int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
        return True
    else:
        return False
    
def checkDayMonthYear(day, month, year):        
    if int(day) < 1 or int(day) > 31:
        return False
    if int(month) < 1 or int(month) > 12:
        return False
    if int(month) in [4, 6, 9, 11] and int(day) > 30:
        return False    
    if int(month) == 2:
        if checkYear(year) == True and int(day) > 29:
            return False
        elif checkYear(year) == False and int(day) > 28:
            return False    
    if int(year) < 1000 or int(year) > 2026:
        return False

    
if checkFormat(date) == False:
    print("yêu cầu nhập đúng định dạng dd/MM/yyyy")
else:
    day, month, year = date.split("/")
    checkDayMonthYear(day, month, year)
    if checkDayMonthYear(day, month, year) == False:
        print("yêu cầu nhập đúng định dạng dd/MM/yyyy")
    elif checkDayMonthYear(day, month, year) == True and checkYear(year) == True:
        print(f"{year} là năm nhuận")
    elif checkDayMonthYear(day, month, year) == True and checkYear(year) == False:
        print(f"{year} không phải là năm nhuận")



