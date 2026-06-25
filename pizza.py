import sys
import csv
import tabulate
def filetype_checker(filename):
    list_file = str(filename).split(".")
    if list_file[1] != "csv":
        print("Wrong file type!")

        sys.exit()
try:
    filename = sys.argv[1]
except IndexError:
    print("too few arguments!")
    sys.exit()
try:
    file = open(filename, "r")
except FileNotFoundError:
    print("file does not exist!")
    sys.exit()
else:
    filetype_checker(filename)
reader = csv.reader(file)
table = []
c = 0
for row in reader:
    if c == 0:
        headers = row
        c = 1
    else:
        table.append(row)
file.close()
print(tabulate.tabulate(table, headers, tablefmt="grid"))

