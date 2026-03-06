
def is_long_enough(pw):
    if len(pw) >= 8:
        return True
    else:
        return False
    
def has_number(pw):
    for i in pw:
        if i >= "0" or i <= "9":
            return True
    return False

def has_uppercase(pw):
    for i in range (1, len(pw)):
        if pw[i] == pw[i].upper() :
            return True
    return False

def is_strong_password(pw):
    if is_long_enough(pw) == True and has_uppercase(pw) == True and has_number(pw) == True:
        return True
    else:
        return False
    