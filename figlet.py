from pyfiglet import Figlet
figlet = Figlet()
import sys
import random

if len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
        f = sys.argv[2]
        figlet.setFont(font = f)
    else:
        sys.exit("Wrong Arguments Given!")
elif len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font = f)

text = input("Enter Text : ")
print(figlet.renderText(text))




