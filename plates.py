
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("invalid")
    else:
        print("Valid")


def is_valid(platenum):
    plate_list = list(platenum)

    if str(platenum).isalnum() is False:
        return True
    elif letter_start(plate_list):
        return True
    elif charlimit(plate_list):
        return True
    elif not check_numbers(plate_list):
        return True
    else: 
        return False
    
def letter_start(l):
    for c in range(2):
        if str(l[c]).isalpha() is False:
            return True
    return False

def charlimit(l):
    n = 0
    for c in l:
        n += 1
    if 2 <= n <= 6:
        return False
    else:
        return True

def check_numbers(s):
    reached_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0" and not reached_number:
                return False  # first number can't be 0
            reached_number = True
        else:
            if reached_number:
                return False  # letter after a number is not allowed
    return True  




main()










