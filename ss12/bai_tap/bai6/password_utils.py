
def is_long_enough(pw):
    if len(pw) >= 8:
        return True
    
def has_number(pw):
    if pw.isdigit() == True:
        return True