from datetime import date
import inflect
import sys


def main():
    input_date = get_date()
    date_1 = date(input_date[0], input_date[1], input_date[2])
    date_2 = date.today()
    min = min_calculator(date_2, date_1)
    print(min, "minutes")



def min_calculator(date_2, date_1):
    difference = date_2 - date_1
    difference = str(difference).split(" ")
    days = int(difference[0])
    minutes =  days * 24 * 60
    p = inflect.engine()
    minutes = p.number_to_words(minutes)
    return minutes

def get_date():
    date = input("Enter your Birthday: ")
    try:
        year, month, day = date.split("-")
    except ValueError:
        sys.exit("Invalid Date")
    else:
        if len(year) != 4 or len(month) != 2 or len(day) != 2:
            sys.exit("Invalid Date!")
        else:
            if int(year) > 2026 or 0 < int(month) > 12 or 0 < int(day) > 31:
                sys.exit("Invalid Date!")
            return int(year), int(month), int(day)

def get_date_today():
    today_date = date.today
    print(today_date)
    


if __name__ == "__main__":
    main()