import csv
students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        


