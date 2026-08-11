"""
Guessing a number game where the user has to guess a randomly generated number between 1 and 100. 
The program provides feedback on whether the guess is too high, too low, or correct. 
The game continues until the user guesses the correct number.
"""
#We use r to indicate that the string is a raw string, which means that backslashes are treated as literal characters and not as escape characters. 
# This is useful for creating ASCII art or other text that contains backslashes.

print(r"""___________                        _________                      __  .__    .__                 
\__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____   
  |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\  
  |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  > 
  |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /  
          \/     |__|        \/          \/             \/     \/          \/        \//_____/   """)

import random


def play_guessing_game():
    """Main function to play the Guessing Game."""
    print("Welcome to the Guessing Game!")

    while True:
        computer_guess_number = random.randint(1, 100)
        user_guess_number = None

        level_of_game = input("Choose a difficulty level (easy,hard): ").lower()
        if level_of_game == "easy":
            attempts = 10
        elif level_of_game == "hard":
            attempts = 5
        else:
            print("Invalid choice. Please select easy or hard.")
            continue
        # continue statement is used to skip the rest of the code inside the loop for the current iteration only.

        print(f"You have {attempts} attempts to guess the number.")
        while user_guess_number != computer_guess_number and attempts > 0:
            try:
                user_guess_number = int(input("Guess a number between 1 and 100: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if user_guess_number < computer_guess_number:
                print("Too low!")
                attempts -= 1
            elif user_guess_number > computer_guess_number:
                print("Too high!")
                attempts -= 1
            else:
                print("Correct! The number was", computer_guess_number)
                break

            if attempts == 0:
                print("You've run out of attempts. The number was", computer_guess_number)

        back_to_game = input("Do you want to play again? (y/n): ").lower()
        if back_to_game != "y":
            break

play_guessing_game()
print("Thanks for playing!")
# So until the break statement is triggered the while loop will keep running and the game will continue to play.
# Here "n" is used to break the loop and exit the game.





    