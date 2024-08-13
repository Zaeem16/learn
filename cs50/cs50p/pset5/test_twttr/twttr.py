def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(word=None):
    if word is None:
        return None
    elif word == int():
        return None
    else:
        for letter in word:
            if letter.lower() in [ 'a', 'e', 'i', 'o', 'u']:
                word = word.replace(letter, '')
        return word


if __name__ == "__main__":
    main()
