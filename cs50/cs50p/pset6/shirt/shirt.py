import sys
import os
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    path_1 = os.path.splitext(sys.argv[1])
    path_2 = os.path.splitext(sys.argv[2])
Valid_types = [".jpg", ".jpeg", ".png"]
if not path_1[1].lower() in tuple(Valid_types):
    sys.exit(f"[{path_1[1]}] is not a valid extension")
elif not path_2[1].lower() in tuple(Valid_types):
    sys.exit(f"[{path_2[1]}] is not a valid extension")
if path_1[1] != path_2[1]:
    sys.exit(f"{path_1[1]} is not the same valid extension as {path_2[1]}")


if not os.path.exists(sys.argv[1]):
    sys.exit(f"file: [{sys.argv[1]}] is not found")

try:
    shirt = Image.open("shirt.png")
    size = shirt.size
    with Image.open(sys.argv[1]) as im:
        photo = ImageOps.fit(im, size=(600,600))
        photo.paste(shirt, shirt)
        photo.save(sys.argv[2])
except (FileNotFoundError, IOError):
    sys.exit("The intended file not found")
