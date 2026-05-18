import random
level = int(input("Level : "))

num = random.randint(1, level)

while True:
    try: 
        guess = int(input("Guess : "))
    except ValueError:
        continue
    
    else:
        if guess == num:
            print("Just Right!")
            break
        elif guess > num:
            print("Too Large!")
        else:
            print("Too small!")

