months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
while True:

    date = input("date : ").strip().title()

    
    if len(date.split()) == 3:
        mon = ""
        num = ""
        for char in list(date):
            if char.isnumeric():
               num = num + char
            elif char.isalpha():
                mon = mon + char
        if len(list(num)) == 6:
            day = num[0:1]
            year = num[2:6]
        elif len(list(num)) == 5:
            day = num[0]
            year = num[1:5]
        try:
            print(f"{year}-{months[mon]}-{day}")
            break
        except KeyError:
            continue
    else:
        try:
            mon, day, year = date.split("/")   
        except ValueError:
            continue
        else:
            print(f"{year}-{mon}-{day}")
            break


