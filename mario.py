def main():
    n = int(input("what size you want ?"))
    print_square(n)

def print_square(d):
    for i in range(d):
        for _ in range(d):
            print("# ", end="")
        print("")
main()    