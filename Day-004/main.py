"""
Topics Covered:

1.Randomisation
2.Lists

"""
import random

print("Welcome to ROCK-PAPER-SCISSORS")

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


list_of_rps = [Rock,Paper,Scissors]
user_input = int(input("What do you want to choose? Type 0 for ROCK - 1 for PAPER - 2 for SCISSORS: "))
if user_input >= 0 and user_input <=2:
    print(list_of_rps[user_input])
computer_input = random.randint(0,2)
print("Computer choice")
print(list_of_rps[computer_input])


if user_input >= 3 or user_input < 0:
    print("YOU TYPED AN INVALID NUMBER")
elif user_input == 0 and computer_input == 2:
    print("YOU WIN!")
elif user_input == 2 and computer_input == 0:
    print("YOU LOOSE")
elif computer_input < user_input:
    print("YOU WIN!")
elif computer_input > user_input:
    print("YOU LOOSE")
elif user_input == computer_input:
    print("IT'S A DRAW!!!")
elif user_input >= 3 or user_input < 0:
    print("YOU TYPED AN INVALID NUMBER")
