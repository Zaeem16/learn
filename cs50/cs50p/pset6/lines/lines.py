import sys
def main():
    print(LOC(sys.argv))



def LOC(file):
    try:
        if len(file) > 2:
            return sys.exit("Too many command-line arguments")
        elif len(file) < 2:
            return sys.exit("Too few command-line argumets")
        elif not file[1].endswith(".py"):
            return sys.exit("Not a python file")
        else:
            with open(file[1], 'r') as file:
                lines = [line for line in file if line.strip() and not line.strip().startswith('#')]
            return len(lines)

    except FileNotFoundError:
        return sys.exit("File not found")


if __name__ == "__main__":
    main()
