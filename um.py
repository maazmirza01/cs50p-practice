import re


def main():
    print(count(input("Text: ")))


def count(text):
    
    matches = re.findall(r" um[m,\.;!?]*", text)
    if (text.lower()).startswith("um"):
        count = 1 
    else:
        count = 0
    for match in matches:
        count += 1
    return count


if __name__ == "__main__":
    main()