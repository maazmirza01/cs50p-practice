while True:
    try:
        x = int(input("Whats x ? "))    # keep the code in the try op as short/minimal as possible./ we could put break under try to too
    except ValueError:
        print("x is not an integer! ERROR!")
    else:
        break


print(f"x is {x}")

# alt way to do this:

def main():
    x = get_int()
    print("x is : ", x)

def get_int():
    while True:
        try:
             x = int(input("Whats x ? ")) 
             break           # keep the code in the try statement as short/minimal as possible./ we could put break under try to too
        except ValueError:
             print("x is not an integer! ERROR!")
    return x

main()
# this is file is notes from my lecture on Exceptions.









