import re

def main():
    print(parse(input("HTML: ")))

def parse(embed):
    if matches := re.search(r'<iframe .*src="https?://(?:www\.)?youtube.com/embed/([0-9A-Za-z]+)" .*></iframe>', embed):
        url = "https://youtu.be/" + matches.group(1)
        return url
    else:
        return None
    

if __name__ == "__main__":
    main()