import csv
import sys

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line argumets")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    elif not sys.argv[2].endswith(".csv"):
        sys.exit("File should be created as csv file")

    else:
        print(change_csv(sys.argv[1], sys.argv[2]))



def change_csv(old_csv, new_csv):
    try:
        with open(old_csv, "r") as rf:
            with open(new_csv, "w") as wf:
                r = csv.DictReader(rf)
                w = csv.DictWriter(wf, fieldnames=["first", "last", "house"])
                w.writeheader()
                for line in r:
                    last, first = line["name"].split(", ")
                    line["first"] = first
                    line["last"] = last
                    del line["name"]
                    w.writerow(line)


    except (FileNotFoundError, IOError):
        sys.exit(f"Couldn't read {old_csv}")





if __name__ == "__main__":
    main()
