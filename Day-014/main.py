"""
This is a python based game called Higer and lower.
In this game, the user has to guess the number which is higher or lower than the given number.

"""
#We are going to split the problem statement into steps and solve it one by one.

# Display Art
from game_data import game_data
print(r"""__  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ ///_/\__, /_/ /_/\___/_/
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /
/_____/\____/|__/|__/\___/_/""")

# Generate a random account from the game data
import random

#Using wile here will make sure that the two accounts are not the same and makes the runs recursive until the two accounts are not the same.
#Format the account data into printable format
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers and guess == 'a':
        return guess == 'a'
    else:
        return guess == 'b'
score = 0
game_is_on = True
#Here in a run the previous account at position B becomes the next account at position A and a new random account is generated at position B.
account_b = random.choice(game_data)
while game_is_on:
    account_a = account_b
    account_b = random.choice(game_data)
    while account_a == account_b:
        account_b = random.choice(game_data)
    print(f"Compare A: {format_data(account_a)}")
    print(r""" _    __
    | |  / /____
    | | / / ___/
    | |/ (__  )
    |___/____(_)""")
    print(f"Against B: {format_data(account_b)}")
    #Ask the user for a guess and check if they got it right.
    ask_user = input("Who has more followers? Type 'A' or 'B': ").lower()
    if ask_user == 'a':
        user_choice = account_a
        other_choice = account_b
    else:
        user_choice = account_b
        other_choice = account_a

    user_followers = user_choice['follower_count']
    other_followers = other_choice['follower_count']
    #Check if the user is correct.
    is_correct = check_answer(ask_user, user_followers, other_followers)

    #Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You are right! {user_choice['name']} has more followers than {other_choice['name']}.score: {score}")
    else:
        print(f"Sorry, {user_choice['name']} has less followers than {other_choice['name']}.score: {score}")
        game_is_on = False

#Game should continue until they get it wrong.





#Scorekeeping.


#make the game repeatable.


#making the account at position B become the next account at position A.


