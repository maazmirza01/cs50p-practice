import sys
from PIL import Image, ImageOps

def same_ext_check(img_name_1, img_name_2):
    ext1 = img_name_1.lower().split(".")[-1]
    ext2 = img_name_2.lower().split(".")[-1]
    return ext1 == ext2

if len(sys.argv) != 3:
    print("Wrong number of arguments")
    sys.exit()

valid_extensions = (".jpg", ".jpeg", ".png")

for arg in sys.argv[1:]:
    if not arg.lower().endswith(valid_extensions):
        print("wrong extension entered!")
        sys.exit()

if not same_ext_check(sys.argv[1], sys.argv[2]):
    print("both images have different filetypes!")
    sys.exit()

img = sys.argv[1]
new_img = sys.argv[2]

try:
    photo = Image.open(img)
except FileNotFoundError:
    print("File Not Found!")
    sys.exit()

photo = ImageOps.fit(photo, size=(600, 600))

shirt = Image.open("shirt.png")
photo.paste(shirt, mask=shirt)

photo.save(new_img)