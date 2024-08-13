def main():
    answer = input("What time it is? ")
    time = convert(answer)
    if time >= 7 and time <= 8:
        print("Breakfast time")
    if time >= 13 and time <= 14 :
        print("Lunch time")
    if time >= 18 and time <= 19 :
        print("Dinner time")


def convert(time):
    hours, minutes = time.split(":")
    new_minutes = float(minutes) / 60
    return float(hours) + new_minutes






if __name__ == "__main__":
    main()

