import sys
import csv

if len(sys.argv) <= 2:
    print("Too few arguments!")
    sys.exit()
elif len(sys.argv) >= 4:
    print("Too many arguments!")
    sys.exit()
file_before = sys.argv[1]
file_after = sys.argv[2]
names = []
houses = []
with open(file_before, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append(row["name"])
        houses.append(row["house"])
dict_names = []
for name in names:
    name_strip = str(name).removesuffix("'").removeprefix("'")
    last, first = name_strip.split(", ")
    dict_names.append({"first": first, "last": last})

with open(file_after, "a") as file:
    writer = csv.DictWriter(file, fieldnames=["first name", "last name", "house"])
    c = 0
    writer.writerow({"first name": "first name", "last name": "last name", "house": "house"})
    for row in dict_names:
        writer.writerow({"first name": row["first"], "last name": row["last"], "house": houses[c]})
        c += 1



