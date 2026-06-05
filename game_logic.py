import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown",
         "programming", "computer", "keyboard", "developer", "terminal"]

MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def get_valid_guess(guessed_letters):
    """Input validation: only accepts a single alphabetical character."""
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter exactly one letter!")
            continue

        if not guess.isalpha():
            print("Please enter a letter, not a number or symbol!")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}', try a different letter!")
            continue

        return guess


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the word progress."""
    print("=" * 40)
    print(STAGES[mistakes])
    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}")

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(f"Word: {display_word}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print("=" * 40)
    print("\n")


def play_game():
    """Main game loop."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("\n🌨️  Welcome to Snowman Meltdown!  🌨️")
    print("Try to guess the word before the snowman melts!\n")

    while mistakes < MAX_MISTAKES:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check if the word is fully guessed
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 You saved the snowman! The word was: " + secret_word)
            return True

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"✅ Good guess! '{guess}' is in the word!")
        else:
            mistakes += 1
            print(f"❌ Wrong! '{guess}' is not in the word! ({mistakes}/{MAX_MISTAKES} mistakes)")

    # Game over - max mistakes reached
    display_game_state(mistakes, secret_word, guessed_letters)
    print("The snowman has melted! The word was: " + secret_word)
    return False


def ask_replay():
    """Asks the user if they want to play again."""
    while True:
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay in ["yes", "y"]:
            return True
        elif replay in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'!")