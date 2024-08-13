import requests
import sys

request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
rate = request.json()["bpi"]["USD"]["rate_float"]

try:
    num = float(sys.argv[1])
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Missing a command-line argument")
    if num:
        amount = rate * num
        print((f"${amount:,.4f}"))
except ValueError:
    sys.exit("Command-line argumnet not a number")
except IndexError:
    sys.exit("Missing a command-line argument")


