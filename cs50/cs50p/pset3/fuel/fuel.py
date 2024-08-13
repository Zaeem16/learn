while True:
    try:
        user_input = input("Fraction: ")
        x, y = user_input.split("/")
        new_x = float(x)
        new_y = float(y)
        if new_x > new_y:
            continue
        if new_y < 1:
            continue
        percentage = new_x / new_y * 100
        if percentage <= 1.0:
            print("E")
            break
        elif percentage >= 99.0:
            print("F")
            break

            print("{:.0f}%".format(percentage))
            break

    except (ValueError, ZeroDivisionError):
        pass




