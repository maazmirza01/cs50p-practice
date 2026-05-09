
def tipcal(bill, tipage):
    tip = bill * tipage / 100
    return tip

def main():
    Amount = float(input("What was the bill ? ").replace("$",""))
    percentage = float(input("Enter tip percentage : ").replace("%", ""))
    T = tipcal(Amount, percentage)
    total = Amount + T

    print("Your tip Amount: $", round(T, 2))
    print("Your total bill Amount: $", round(total, 2))

print("Tip Calculator :")
print("Hello, Customer!")
main()




