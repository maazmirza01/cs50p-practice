grocery_list = {}
while True:
    try:
        item = input().upper().strip()
    except EOFError:
        break
    else:
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
print("\n")


for i in sorted(grocery_list):
    print(grocery_list[i], i) 


