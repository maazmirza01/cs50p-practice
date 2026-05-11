
due = 50
def coin_receiver():
    A = int(input("Insert Coin! : "))
    while True:
        if A == 25 or A == 10 or A == 5:
            break
        else:
            A = int(input("Invalid Coin Enter Again! :"))
    return A

while due > 0:
    print(f"Amount Due: {due}")
    amount = coin_receiver()
    due = due - amount


due = due * (-1)
print(f"change owed: {due}")    


