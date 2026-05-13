d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
key_list = []

def total_printer(k):
    total = 0
    for item in k:
        total = total + d[item]
    print(f"your Total : $ {total: .2f}")


while True:
    try:
        key = input("Order! : ").title().strip()
    except EOFError:
        print(None)
        break
    else:
        
        if key in list(d):
            key_list.append(key)
            total_printer(key_list)    
        else:
            print("Wrong menu item enter again!")
            


