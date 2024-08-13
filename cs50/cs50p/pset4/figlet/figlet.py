from pyfiglet import Figlet
from pyfiglet import FigletFont
import sys
import random



random = random.Random()

if len(sys.argv) != 3 and len(sys.argv) != 1:
    sys.exit("Invalid usage")
if sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("Invalid usage")
if sys.argv[2] not in FigletFont.getFonts():
    sys.exit("Invalid usage")



if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = Figlet(font=sys.argv[2])
        msg = input("Input: ")
        print(f.renderText(msg))

elif len(sys.argv) == 1:
    msg = input("Input: ")
    fonts = FigletFont.getFonts()
    f = Figlet(font=random.choice(fonts))
    print(f.renderText(msg))







