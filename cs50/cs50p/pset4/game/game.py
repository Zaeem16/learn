import random


while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            pass
        elif level > 0:
            ran_int = random.randint(1, level)
            break
    except ValueError:
        pass


while level > 0:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            pass
        elif guess > 0:
            if guess == ran_int:
                print("Just right!")
                break
            elif guess > ran_int:
                print("Too large!")
                pass
            elif guess < ran_int:
                print("Too small!")
                pass
    except ValueError:
        pass

