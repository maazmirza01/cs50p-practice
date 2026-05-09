print("Whats your Greeting ?")
greeting = input().lower().strip()

def first_word(t):
    return str(t).startswith("hello")

def first_letter(t):
    return str(t).startswith("h")

if  first_word(greeting):
    print("you win $ 0.")
elif first_letter(greeting):
    print("You win $ 20.")
else:
    print("You win $ 100.") 
