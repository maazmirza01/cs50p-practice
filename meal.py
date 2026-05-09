time = input("What's the time right now ? ")

def main(t):
    mealtime = convert(t)

    if 7 <= mealtime <= 8:
        m = "breakfast"
    elif 12 <= mealtime <= 13:
        m = "lunch"
    elif 18 <= mealtime <= 19:
        m = "dinner"
    else:
        m = "no time"
    
    return m
    


def convert(time):
    hour, minute = str(time).split(sep=":")
    hour_num = float(hour)
    min_num = float(minute)

    converted_time = hour_num + (min_num / 60)
    return converted_time

meal = main(time)
 
if meal == "breakfast":
    print("Its time for your breakfast!")
elif meal == "lunch":
    print("Its time for your lunch!")
elif meal == "dinner":
    print("Its time for your dinner!")  
else:
    print("Not the time to eat!")    















