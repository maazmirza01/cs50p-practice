import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(hours):
    if matches := re.search(r"([0-9]{1,2}):?([0-9]{2})? (AM|PM) to ([0-9]{1,2}):?([0-9]{2})? (AM|PM)", hours):
        if 1 > int(matches.group(1)) > 12:
            raise ValueError
        elif 1 > int(matches.group(4)) > 12:
            raise ValueError
        elif int(matches.group(2)) > 59:
            raise ValueError
        elif int(matches.group(5)) > 59:
            raise ValueError
        else:
            if matches.group(3) == "PM" and matches.group(1) != "12":
                hour_start = int(matches.group(1)) + 12
                hour_end = matches.group(4)
            elif matches.group(6) == "PM" and matches.group(4) != "12":
                hour_end = int(matches.group(4)) + 12
                hour_start = matches.group(1)
            else:
                hour_end = matches.group(4)
                hour_start = matches.group(1)
            if matches.group(3) == "AM" and matches.group(1) == "12":
                hour_start = "00" 
                
            elif matches.group(6) == "AM" and matches.group(4) == "12":
                hour_end = "00"
        final = f"{hour_start}:{matches.group(2)} to {hour_end}:{matches.group(5)}"
        return final
            
    
    else:
        raise ValueError
    


...


if __name__ == "__main__":
    main()