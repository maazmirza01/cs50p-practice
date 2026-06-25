import sys
try:
    filename = sys.argv[1]
except IndexError:
    print("Too few arguments!")
    sys.exit()
try:
    with open(filename, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not Found!")
    sys.exit()
else:
    num = len(lines)
    print(num)