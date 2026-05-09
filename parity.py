def main():
    x = int(input("Whats X ? "))

    if alt2_is_even(x):
        print("X is even!")
    else:
        print("X is odd!")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def alt_is_even(n):
    return True if n % 2 == 0 else False

def alt2_is_even(n):
    return n % 2 == 0


main()