import sys
import csv
from tabulate import tabulate


def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        else:
            print(csv_indecator(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File not found")



def csv_indecator(filename):
    try:
        if not filename.endswith(".csv"):
            sys.exit("Not a csv file")
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        with open(filename, "r") as file:
            file_reader = csv.reader(file)
            return tabulate(file_reader, headers="firstrow", tablefmt="grid")


if __name__ == "__main__":
    main()
