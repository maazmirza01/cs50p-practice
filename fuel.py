while True:
    try:
        fraction = input("Input a fraction: ")
        num, den = fraction.split("/")  # split into numerator and denominator
        num = int(num)
        den = int(den)
        
        if den == 0:
            raise ZeroDivisionError
        
        f = num / den
        
        if 0 <= f <= 1:  # valid fraction must be between 0 and 1
            break
        else:
            print("Fraction must be between 0 and 1, try again!")
            
    except (ValueError, ZeroDivisionError):
        print("Try again! Wrong value entered")

p = round(f * 100)

if p == 100:
    print("F")
elif p == 0:
    print("E")
else:
    print(f"{p}%")