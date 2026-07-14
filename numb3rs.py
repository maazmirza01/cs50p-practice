import re


def main():
    if not validate(input("IPv4 Address: ")):
        print("False")
    else:
        print("True")
    


def validate(ip):
    matches = re.search(r"([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", ip)
    if matches:
        for c in range(4):
            if 0 <= int(matches.group(c + 1)) <= 255:
                continue
            else:
                return False
    else:
        return False


if __name__ == "__main__":
    main()