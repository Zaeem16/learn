def main():
    while True:
        try:
            user_input = input("Fraction: ")
            percentage = gauge(convert(user_input))
            print(percentage)
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = map(int, fraction.split("/"))
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    percentage = round(x / y * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return "{:.0f}%".format(percentage)



if __name__ == "__main__":
    main()
