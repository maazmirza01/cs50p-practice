import emoji

t = input("Input: ").lower().strip()
print(emoji.emojize(f"Output: :{t}:", language ="alias"))