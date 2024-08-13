import sys
import csv
from tabulate import tabulate


def main():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            print(pretty_csv(sys.argv[1], sys.argv[2]))
    except FileNotFoundError:
        sys.exit("File not found")
    except tabulate.TabulateError:
        sys.exit("Invalid Table Type")




def pretty_csv(filename, fonttype):
    try:
        if not filename.endswith(".csv"):
            sys.exit("Not a csv file")
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        with open(filename, "r") as file:
            file_reader = csv.reader(file)
            return tabulate(file_reader, headers="firstrow", tablefmt=fonttype)


if __name__ == "__main__":
    main()
