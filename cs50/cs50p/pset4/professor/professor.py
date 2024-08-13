import random


def main():
    level = get_level()
    generate_integer(level)

levels = [1, 2, 3]
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in levels:
                pass
            elif level in levels:
                return level
        except ValueError:
            pass




def generate_integer(level):
    n = 10
    m = 0
    score = 0
    while m < n:
        try:
            if level == 1:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                z = x + y
                for _ in range(3):
                    k = int(input(f"{x} + {y} = "))
                    if k == z:
                        n -= 1
                        score += 1
                        break
                    else:
                        print("EEE")

                if k != z:
                    print(f"{x} + {y} = {z}")
                    n -= 1
            elif level == 2:
                x = random.randint(10, 99)
                y = random.randint(10, 99)
                z = x + y
                for _ in range(3):
                    k = int(input(f"{x} + {y} = "))
                    if k == z:
                        n -= 1
                        score += 1
                        break
                    else:
                        print("EEE")

                if k != z:
                    print(f"{x} + {y} = {z}")
                    n -= 1

            elif level == 3:
                x = random.randint(100, 999)
                y = random.randint(100, 999)
                z = x + y
                for _ in range(3):
                    k = int(input(f"{x} + {y} = "))
                    if k == z:
                        n -= 1
                        score += 1
                        break
                    else:
                        print("EEE")

                if k != z:
                    print(f"{x} + {y} = {z}")
                    n-= 1
                    
            if m == n:
                print(score)
                break
        except ValueError:
            print("EEE")
            pass







if __name__ == "__main__":
    main()
