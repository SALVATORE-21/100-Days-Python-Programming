"""
The BlackJack game is a popular card game where players try to get a hand value as close to 21 as possible without going over. In this implementation, we will create a simple version of the game where a player can play against the dealer.
1. When a card is drawn from the deck, it is not removed from the deck to prevent running out of cards.
2. The player can choose to "hit" (draw another card) or "stand" (keep their current hand).
3. The dealer will draw cards until their hand value is 17 or higher.
"""
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Ace is represented as 11

#Function deal_card() to randomly select a card from the deck
def deal_card():
    """Returns a random card from the deck."""
    card = random.choice(cards)
    return card

def play_blackjack():
    """Main function to play the Blackjack game."""
    user_cards = []
    computer_cards = []
    game_over = False

    #Now we will deal two cards to the user and the computer at the start of the game.
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #We cannot use += to add the card to the list because it will throw an error coz += expects an iterable. Instead, we use the append() method to add the card to the list.
    def calculate_score(cards):
        """Calculates the score of the given hand of cards."""
        if sum(cards) == 21 and len(cards) == 2:
            return 0  # Blackjack
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)


    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        game_over = False

    if not game_over:
        while user_score < 21:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards}, current score: {user_score}")
            else:
                break

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    def compare(user_score, computer_score):
        """Compares the scores of the user and the computer to determine the winner."""
        if user_score > 21 and computer_score > 21:
            return "You went over. You lose 😤"
        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_blackjack()
