"""Hangman Game - CodeAlpha Python Internship (Task 1)

A simple text-based Hangman game.
Concepts used: random, while loop, if-else, strings, lists.
"""

import random

WORDS = ["python", "internship", "program", "keyboard", "developer"]
MAX_WRONG = 6


def display_word(word, guessed):
    """Return the word with unguessed letters hidden as underscores."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word one letter at a time. You can miss {MAX_WRONG} times.\n")

    while wrong < MAX_WRONG:
        print("Word:", display_word(word, guessed))
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print("Guessed letters:", " ".join(guessed) if guessed else "none")

        guess = input("Enter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong += 1
            print("Wrong guess!\n")

        # Win check
        if all(letter in guessed for letter in word):
            print("Word:", display_word(word, guessed))
            print(f"Congratulations, you won! The word was '{word}'.")
            return

    print(f"Game over! You ran out of guesses. The word was '{word}'.")


if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
        print()
