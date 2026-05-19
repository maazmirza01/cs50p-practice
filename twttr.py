
def main():
    txt = input("Enter your tweet here : ")
    short_text = shorten_word(txt)
    print(short_text)

def shorten_word(t):
    text = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for char in t:
        if char not in vowels:
            text = text + char
    return text

if __name__ == "__main__":
    main() 









