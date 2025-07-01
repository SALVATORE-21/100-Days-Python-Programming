import random

print("==== HANGMAN GAME ====")

# List of words to choose from
word_list = ['AMERICA', 'INDIA', 'RUSSIA']
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
lives = word_length  # Total attempts
guessed_letters = []
display = ["_"] * word_length

# Game loop
while lives > 0 and "_" in display:
    print("\nCurrent word:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Enter a single alphabet only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good guess!")
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(f"❌ Wrong guess! Lives left: {lives}")

# Final result
if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The word was:", chosen_word)
