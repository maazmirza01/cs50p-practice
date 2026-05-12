inventory = {
    "shirt": 1500,
    "pants": 2500,
    "shoes": 4000,
    "hat": 1000,
    "glasses": 2000,
}

def main():
    cart = cart_maker()
    cart_displayer(cart, inventory)
    total = cost_calculator(cart, inventory)
    expensive_item_printer(cart, inventory)
    print(f"Your total cost is : $ {total}")
    cashier(total)

def cart_maker():
    items = ["shirt", "pants", "shoes", "hat", "glasses"]
    cart = []
    while True:
        item_name = input("What would you like to order ? ").lower().strip()
        if item_name in items:
            cart.append(item_name)
            x = input("Press 'Y' if you'd like to order again! else press enter! ").lower().strip()
            if x != "y":
                break
            else:
                continue
        else:
            print("Item not available, Try again!")
    return cart

def cart_displayer(cart_list, inventory_items):
    for item in cart_list:
        print(f"Item: {item} - $ {inventory_items[item]}")

def cost_calculator(cart_items, inventory_total):
    bill = 0
    for item in cart_items:
        bill = bill + inventory_total[item]
    
    return bill

def expensive_item_printer(in_cart, in_inventory):
    ex_item = "hat"
    for item in in_cart:
        if in_inventory[ex_item] < in_inventory[item]:
            ex_item = item
    
    print(f"your most expensive item is {ex_item}")

def cashier(c):
    while c > 0:
         print(f"Amount Due: {c}")
         amount = coin_receiver()
         c = c - amount


    c = c * (-1)
    print(f"change owed: {c}")  
    


def coin_receiver():
    A = int(input("Insert Coin! : "))
    available_coins = [5000, 1000, 500, 200]
    while True:
        if A in available_coins:
            break
        else:
            A = int(input("Invalid Coin Enter Again! :"))
    return A


main()
