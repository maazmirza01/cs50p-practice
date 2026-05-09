print("House Finder!")
name = input("Who is your character? ").lower()

match name:
    case "harry" | "ron" | "hermione":
        print("Gryffindor!")
    case "draco":
        print("slytherin!")
    case _:
        print("who?")
