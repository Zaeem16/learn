import re



def main():
    print(count(input("Text: ")))



def count(string):
    pattern = r"((?<![a-z])um(?![a-z]))*"
    match = re.findall(pattern, string.lower())
    count_matches = match.count("um")
    print(match)
    return count_matches



if __name__ == "__main__":
    main()
