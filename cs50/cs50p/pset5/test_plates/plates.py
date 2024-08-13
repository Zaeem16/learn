def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0].isalpha() == False and s[1].isalpha() == False:
        return False
    if s.isalnum() == False:
        return False
    if len(s) < 2 or len(s) > 6:
        return False

    i = 0
    while i < len(s) :
        if s[i].isalpha() == False :
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    flag = False
    for c in s:
        if c.isdigit():
            flag = True
        if flag is True and c.isalpha():
                return False
    return True



if __name__ == "__main__":
    main()

