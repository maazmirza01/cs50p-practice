
x = float(input("What is the first number? "))
y = float(input("What is the second number? "))
z = round(x / y, 2) # how to round a number to a specific number of decimal places

print(f"{z:,}") # how to format a number with commas as thousands separators, and how to use f-strings to include variables in a string without concatenation


def square(n):
    return n * n # how to define a function that returns a value, and how to use the return statement to return a value from a function
def main():
    num = int(input("What is your number? "))
    print(f"Square of your {num} is", square(num)) # how to call a function with an argument, and how to use f-strings to include variables in a string without concatenation



main()