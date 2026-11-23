
import random

DIFFICULTY_LEVELS = {
    "easy": 10,
    "medium": 7,
    "hard": 5
}


def choose_difficulty():
    print("\nChoose your difficulty:")
    print("1. Easy   (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard   (5 attempts)")

    choices = {
        "1": "easy",
        "2": "medium",
        "3": "hard"
    }

    while True:
        choice = input("\nYour choice: ").strip().lower()

        if choice in choices:
            return choices[choice]

        if choice in DIFFICULTY_LEVELS:
            return choice

        print("Hmm, that's not a valid choice. Try again!")


def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))

            if 1 <= guess <= 100:
                return guess

            print("Please enter a number between 1 and 100.")

        except ValueError:
            print("That's not a valid number. Give it another try!")


def play_game():
    print("\n" + "=" * 35)
    print("      WELCOME TO NUMBER GUESS!")
    print("=" * 35)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you figure out what it is?")

    difficulty = choose_difficulty()
    attempts_allowed = DIFFICULTY_LEVELS[difficulty]

    secret_number = random.randint(1, 100)

    print(f"\nGreat! You chose {difficulty.upper()} mode.")
    print(f"You have {attempts_allowed} attempts. Good luck!")

    for attempt in range(1, attempts_allowed + 1):
        print(f"\nAttempt {attempt}/{attempts_allowed}")
        guess = get_guess()

        if guess < secret_number:
            print("Too low! Try going a little higher.")

        elif guess > secret_number:
            print("Too high! Try something lower.")

        else:
            print(f"\nYou got it! The number was {secret_number}.")
            print(f"You figured it out in {attempt} attempt(s)!")
            break

    else:
        print("\nOut of attempts! Better luck next time.")
        print(f"The secret number was {secret_number}.")

    print("\nThanks for playing! See you again.")


if __name__ == "__main__":
    play_game()
