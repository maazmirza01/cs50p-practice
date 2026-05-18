import inflect
p = inflect.engine()

name_list = []
while True:
    try:
        name = input("Name : ").title().strip()
    except EOFError:
        break
    else:
        name_list.append(name)

second_list = []
for n in name_list:
    second_list.append(n)
    print("Adieu, adieu, to", p.join(second_list))




