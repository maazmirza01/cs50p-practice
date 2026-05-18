import random


def main():
    l = get_level()
    for _ in range(10):
        c = 0
        x = generate_integer(l)
        y = generate_integer(l)
        while True:
            try:
                A = int(input(f"{x} + {y} = "))
            except ValueError:
                continue
            else:
                c += 1
                if A == x + y:
                    break
                elif A != x + y and c == 3:
                    print(f"{x} + {y} = {x + y}")
                    break
                elif A != x + y:
                    print("EEE")
                    
                


def get_level():
    while True:
        try:
            level = int(input("Enter Level (1-3) : "))
        except ValueError:
            continue
        else:
            if 1 <= level <= 3:
                break
            else:
                print("Wrong input, try again!")
    return level
    


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()