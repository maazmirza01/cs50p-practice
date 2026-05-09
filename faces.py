def main():
    text = input("Write something : ").strip()
    print(convert(text))

def convert(s):
    return s.replace(":)", "🙂").replace(":(", "🙁")

main()