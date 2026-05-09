
print("Write the Arithmetic expression you'd like to solve :)")
expression = str(input()).strip().lower()

def calculator(a, b, c):
    match b:
        case "x" | "*":
            ans = a * c
        case "/":
            ans = a / c
        case "+":
            ans = a + c
        case "-":
            ans = a - c
        case _:
            ans = "you entered an invalid expression!"
    
    return ans

first, second, third = expression.split()

num_1 = float(first)

num_2 = float(third)

answer = calculator(num_1, second, num_2)

if answer == "you entered an invalid expression!":
    print(answer)
else:
    print("Your answer is : ", round(answer, 1))