#importing necessary libraries
import random
import json
import sys
import os
from time import sleep

class modeError(Exception):
    pass

class systemExitError(Exception):
    pass

# the variables that can only be read in entire program
modes = ["Easy", "Medium", "Hard", "Impossible"]
quit = "Q"

#opening the json file so to have access to all countries and hints
with open("all_countries.json", "r") as jf:
    my_countries = json.load(jf)


#handling all the logic of this program by main
def main():
   try:
       dashboard()
       mode = mode_selector()
       os.system("clear")
       print("Starting the game...")
       sleep(2)
       print("The game started!")
       run_mode(mode)

   except systemExitError:
       sys.exit()
   except modeError:
       print("Invalid mode. Please try again.")







#a dashboard that showed be shown when the program is running
def dashboard():
    print('""' * 41 )
    print('""""                  Welcome to the country Guessing Game!                  """""')
    print('""""                                                                         """""')
    print('""""                               RULES!                                    """""')
    print('""""         1. based on the chosen Mode you will be given limited           """""')
    print('""""            attempts and hints and to guess the correct country.         """""')
    print('""""         2. There are four modes Easy, Medium, Hard, and Impossible!     """""')
    print('""""                                                                         """""')
    print('""""                              Reminder!                                  """""')
    print('''""""                Type 'Q' at any point to quit the game                   """""''')
    print('""' * 41)



#return the selected mode
def mode_selector():
    while True:
        mode = input(f"Which Mode do you wanna play? ").strip().lower()
        if mode.capitalize() in modes:
            return mode
        elif mode == quit or mode == quit.lower():
            raise systemExitError
        else:
            raise modeError



#logic of the country guessing game
def play_game(attempts):
    #generate a random country
    random_key = random.choice(list(my_countries.keys()))
    hints = my_countries[random_key]

    #based on the number of guesses provide hints and chances to guess.
    for i in range(attempts):
        yield f"\nHint {i + 1}: {hints[i]}"
        country_guess = input("Your guess: ").strip().lower()

        if country_guess == quit or country_guess == quit.lower():
            raise systemExitError

        if country_guess == random_key.lower().strip():
            yield "\nWell done! You guessed it.🥳\n"
            break

        else:
            attempts -= 1
            yield f"\nAttempts remaining: {attempts}"


        if attempts == 0:
            yield f"The country was {random_key}. Better luck next time!😁\n"
            break

#based on the mode run the game
def run_mode(mode):
    print(f"\nThe game is in: {mode.capitalize()} mode")
    mode_num = {
        "easy" : 5,
        "medium" : 4,
        "hard" : 3,
        "impossible" : 1
        }
    while True:
        number = mode_num[mode]
        for event in play_game(number):
            print(event)
        again = play_again()
        if again == True:
            mode = mode_selector()
        else:
            raise systemExitError


# 
#ask if they wanna play again
def play_again():
    user_input = input("Do you wanna play again? (yes/no) ").strip().lower()
    if user_input == "yes":
        return True
    else:
        return False


#When importing the functions from this file just making sure to not import main unless the __name__ is __main__. IDK what __name__ is
if __name__ == "__main__":
    main()
