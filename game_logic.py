import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the word progress."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    """Main game loop."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while mistakes < MAX_MISTAKES:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check if the word is fully guessed
        if all(letter in guessed_letters for letter in secret_word):
            print("You saved the snowman! The word was: " + secret_word)
            return

        guess = input("Guess a letter: ").lower()

        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter, try again!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            mistakes += 1
            print(f"Wrong! The snowman is melting! ({mistakes}/{MAX_MISTAKES} mistakes)")

    # Game over - max mistakes reached
    display_game_state(mistakes, secret_word, guessed_letters)
    print("The snowman has melted! The word was: " + secret_word)