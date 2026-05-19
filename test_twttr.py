from twttr import shorten_word

def main():
    test_shorten()

def test_shorten():
    assert shorten_word("Hellow My Name is Maaz") == "Hllw My Nm s Mz"
    assert shorten_word("Hermione") == "Hrmn"
    assert shorten_word("Jon") == "Jn"
    assert shorten_word("harry") == "hrry"

if __name__ == "__main__":
    main()