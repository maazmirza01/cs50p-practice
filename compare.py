x = float(input("Enter your grade: "))

print("Your Grade is: ", end = " ")

if x >= 90:
    print("A*")
    print("Congratulations!")
elif x >= 80:
    print("A")
    print("Congratulations!")
elif x >= 70:
    print("B")
    print("Goog Job!")
elif x >= 60:
    print("C")
    print("Could Improve")
elif x >= 50:
    print("D")
    print("Barely Made it.")
else:
    print("U")
    print("Failed!")