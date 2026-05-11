"""
students = ["harry", "ron", "hermione", "draco"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])

"""
students = {
    "hermione": "Gryfindor",
    "harry": "Gryffindor",
    "ron": "Gryffindor",
    "draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=", ")

students = [
    {"name:": "hermione", "house:": "Gryffindor", "patronus:": "otter"},
    {"name:": "harry", "house:": "Gryffindor", "patronus:": "Stag"},
    {"name:": "ron", "house:": "Gryffindor", "patronus:": "Jack Russell Terrier"},
    {"name:": "Draco", "house:": "Slytherin", "patronus:": None}
]

for student in students:
    print(student["name:"], student["house:"], student["patronus:"], sep=", ")