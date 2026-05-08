print("hello, world!") # first line ever written in python

name = input("what's your name? ") # how to make a variable

name = name.strip().capitalize() # how to remove whitespace from the beginning and end of a string and how to capitalize the first letter of a string

print("hello,", name + ",", "You are awesome!") #how to print multiple things at once, and how to concatenate strings with variables

print('hello,', end=' ', sep='') # how to change the end of a print statement, and how to change the separator between items in a print statement

print(name + "!") # how to use the end and sep parameters in a print statement to create a custom output format

print("have a \"beautiful\" Day!") # how to use escape characters to include special characters in a string, such as quotes or newlines

print(f"hello, {name}!") # how to use f-strings to include variables in a string without concatenation

name = input("what's your name? ").strip().title()

first, last = name.split()
print(f"hello, {last}!") # how to split a string into multiple variables, and how to use the title() method to capitalize the first letter of each word in a string



def hello(to="world"): # how to define a function in python, and how to use default parameters
    print("hello", to) # how to define a function in python, and how to call a function

def main():
    newname = input("what's your new name? ")
    hello(newname)
    def goodbye(to="world"):
        print("goodbye", to)   # how to call a function that is defined inside another function, and how to use default parameters in a function


main()