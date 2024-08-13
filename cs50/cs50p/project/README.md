# Country guessing game
#### Video Demo: <URL HERE>
#### Description:
Hello! In my final project for the CS50 introduction to programming with python I decided to make a game. After thinking about different options I finally decided to make a game that you guess the country based on the given hints. I decided to give this game features such as hints, attemtps, and mode to make it more fun and engaging. Then I made the logic of the game as following:

1. I created a dashboard that welcomes the user, shows the rules, and reminders about my game. And the rules and reminders are:
   * The mode of the game should be one of the following: Easy, Medium, Hard, and Impossible.
   * based on the chosen Mode you will be given limited attempts and hints to guess the correct country.
   * type "q" or "Q" to quit the game at any point

2. I then prompt the user for a mode and the mode can be the one of the four following: Easy, Medium, Hard, and Impossible. after prompting the user for mode if the inputted mode is valid then the program clears the terminal using the **os module** else prints "Invalid mode. Please try again." and prompts the user again for a valid mode.

3. After that, My game prints "Starting the game" and I pause right there for two seconds using **time module** to give the "_vibes_" of real game. then i print "The game is started" to avoid confusion.

4. Then my program generates a random country using the **random module** and the **all_countries.json** file.
    - all_countries.json file is a dictionary json file that contains basically all the countries as keys and a list of 5 hints as values of that country.

5. Then, my program prompts the user "Your guess: " for thier guess based on the mode. This process of guessing repeates as following:
    * **Easy mode:** 5 attempts and 5 hints.
    * **Medium mode:** 4 attempts and 4 hints.
    * **Hard mode:** 3 attempts and 3 hints.
    * **Impossible mode:** 1 attempt and 1 hint.

6. if the user guessed correctly then "Well done. You guessed it.🥳" will be printed or if they run out of attempts then my code will print f"The country was {random_key}. Better luck next time!😁\n" where random_key is a generated random country.

7. After every guess a user makes the number of attempts remaining will be shown to them.

8. Either the user guessed correctly or run out of attempts they will be prompted if they wanna play again.
    - If yes then they will be prompted which mode they wanna play.
    - if no or anything else then the program will exit.

9. All the modules that I used:
    - **random module**
        - to generate a random key (country) and to store the values (hints) of that country.
    - **json**
        - to store the data of all the countries and hints of for that country
    - **sys**
        - to exit the program when needed
    - **os**
        - to clear the terminal when the game is started (after mode selection for the first time)
    - **time**
        - to pause the program for 2 seconds when the game starts (after mode selection for the first time)

10. The point of my each File in my project directory:
    - **project.py:** The main file where all the logic of my country guessing game is in python.
        - contains 5 modules
            - listed above

        - 2 classes that are my custom errors
            - modeError class
            - systemExitError class

        - my_country dictionary that contains the json file data.

        - 6 functions
            - main
                - wraps all of my game logic in one place.

            - dashboard
                - a little dashboard to guide the user when the program runs.

            - play_game
                - the main logic of the game itself.

            - play_again
                - prompting the user if they wanna play again.

            - run_mode
                - run the game based on the chosen mode.

            - mode_selector
                - return the inputted mode.


    - **test_project.py:** contains the test of most of my functions with different scenarios .

        - tests 4 of my functions (testable functions)
            - test_play_again
            - test_run_mode
            - test_mode_selector
            - test_play_game

        - 11 tests
            - 2 tests for test_play_again
            - 6 tests for test_mode_selector
            - 2 test for test_play_game
            - 1 test for test_run_mode

        - unittest.mock
        - pytest

    - **requirement.txt:** A file that I created but does not have any data because non of the modules i used are pip installable modules. All the used modules are Standard python module that comes with the language.
        - no data (not needed)

    - **all_countries.json:** A .json file that i use to generate a random country and hints about the country.
        - contains uncountedly every country in the world as keys and a list as a value that contains hints about the key (the country).

    - **README.md:** An .md file that explains everything in my project detailed.
        - My projects description in detail
        - My used modules
        - The job of each of my files that I used to make this program happen.

11. My program is case-insensitive and white-space-insensitive. So "Easy" and "easy" are the same.


