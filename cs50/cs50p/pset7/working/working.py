import re


def main():
    print(convert(input("Hours: ")))


def convert(time):
    PM_timings = {

        "1"	: "13",
        "2"	: "14",
        "3"	: "15",
        "4"	: "16",
        "5"	: "17",
        "6"	: "18",
        "7"	: "19",
        "8"	: "20",
        "9"	: "21",
        "10" : "22",
        "11" : "23",
        "12" : "12"
}
    AM_timings = {
        "1"	: "01",
        "2"	: "02",
        "3"	: "03",
        "4"	: "04",
        "5"	: "05",
        "6"	: "06",
        "7"	: "07",
        "8"	: "08",
        "9"	: "09",
        "10" : "10",
        "11" : "11",
        "12" : "00"
}

    pattern = r"^([0-9]|[0-1]?[0-2])([: ]?)((?:[0-5][0-9])?) ((?:A|P)M)( to )([0-9]|[0-1]?[0-2])([: ]?)((?:[0-5][0-9])?) ((?:A|P)M)$"
    match = re.search(pattern, time)
    if not match:
        raise ValueError
    elif match.group(4) == "PM" and match.group(9) == "PM":
        hour1 = PM_timings[match.group(1)]
        min_sec1 = match.group(3)
        hour2 = PM_timings[match.group(6)]
        min_sec2 = match.group(8)
        if min_sec1 == "":
            min_sec1 = "00"
        if min_sec2 == "":
            min_sec2 = "00"
        return f"{hour1}:{min_sec1} to {hour2}:{min_sec2}"

    elif match.group(4) == "PM" and match.group(9) == "AM":
        hour1 = PM_timings[match.group(1)]
        min_sec1 = match.group(3)
        hour2 = AM_timings[match.group(6)]
        min_sec2 = match.group(8)
        if min_sec1 == "":
            min_sec1 = "00"
        if min_sec2 == "":
            min_sec2 = "00"
        return f"{hour1}:{min_sec1} to {hour2}:{min_sec2}"

    elif match.group(4) == "AM" and match.group(9) == "AM":
        hour1 = AM_timings[match.group(1)]
        min_sec1 = match.group(3)
        hour2 = AM_timings[match.group(6)]
        min_sec2 = match.group(8)
        if min_sec1 == "":
            min_sec1 = "00"
        if min_sec2 == "":
            min_sec2 = "00"
        return f"{hour1}:{min_sec1} to {hour2}:{min_sec2}"

    elif match.group(4) == "AM" and match.group(9) == "PM":
        hour1 = AM_timings[match.group(1)]
        min_sec1 = match.group(3)
        hour2 = PM_timings[match.group(6)]
        min_sec2 = match.group(8)
        if min_sec1 == "":
            min_sec1 = "00"
        if min_sec2 == "":
            min_sec2 = "00"
        return f"{hour1}:{min_sec1} to {hour2}:{min_sec2}"




if __name__ == "__main__":
    main()