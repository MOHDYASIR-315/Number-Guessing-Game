# Number Guessing Game

A simple, interactive, and beginner-friendly command-line game built with **Python**. Test your guessing skills by finding a randomly generated number between 1 and 100 before running out of attempts!

Choose your difficulty level, follow the hints, and see how quickly you can guess the secret number.

---

## Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Difficulty Levels](#-difficulty-levels)
- [Getting Started](#-getting-started)
- [How to Play](#-how-to-play)
- [Sample Outputs](#-sample-outputs)
- [Project Structure](#-project-structure)
- [Concepts Used](#-concepts-used)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## About the Project

The Number Guessing Game is a command-line Python application where the computer randomly selects a secret number between **1 and 100**, and the player has to guess it within a limited number of attempts.

After every guess, the game provides helpful hints:

- **Too Low:** Your guess is smaller than the secret number.
- **Too High:** Your guess is greater than the secret number.
- **Correct Guess:** Congratulations! You've found the secret number.

The game also includes multiple difficulty levels and input validation to provide a smoother playing experience.

---

## Features

- **Three Difficulty Levels:** Choose between Easy, Medium, and Hard.
- **Random Number Generation:** Every game generates a new secret number.
- **Limited Attempts:** Each difficulty level comes with a different attempt limit.
- **Helpful Hints:** Get feedback after every incorrect guess.
- **Input Validation:** Handles invalid inputs and out-of-range guesses.
- **Interactive Interface:** Simple, friendly, and easy-to-understand terminal messages.
- **Modular Code Structure:** Uses separate functions to keep the code organized and maintainable.

---

## Difficulty Levels

The game offers three difficulty settings:

| Difficulty | Maximum Attempts | Challenge |
|:---:|:---:|:---|
|  Easy | 10 | Beginner-friendly |
|  Medium | 7 | Moderate challenge |
|  Hard | 5 | Limited chances |

Choose your difficulty wisely. The fewer attempts you have, the more carefully you'll need to think before guessing!

---

## Getting Started

Follow these steps to run the project on your local machine.

### Prerequisites

- Python 3.8 or higher recommended.
- A terminal or command-line interface.
- No external Python libraries are required.

### 1. Clone the Repository

```bash
git clone https://github.com/MOHDYASIR-315/Number-Guessing-Game.git
```

### 2. Navigate to the Project Directory

```bash
cd number-guessing-game
```

### 3. Run the Program

```bash
python main.py
```

If your system uses `python3` instead, run:

```bash
python3 main.py
```

---

## How to Play

1. Start the program using Python.
2. Select a difficulty level:
   - Enter `1` for Easy.
   - Enter `2` for Medium.
   - Enter `3` for Hard.
   - You can also enter the difficulty name directly.
3. Enter a number between 1 and 100.
4. Read the hint displayed after each guess.
5. Continue guessing until you find the secret number or run out of attempts.
6. Enjoy the result!

**Note:** Invalid inputs are rejected, and you are asked to enter a valid guess without consuming an attempt.

---

## Sample Outputs

### Example 1: Successful Game (Easy Mode)

```text
===================================
      WELCOME TO NUMBER GUESS!
===================================
I'm thinking of a number between 1 and 100.
Can you figure out what it is?

Choose your difficulty:
1. Easy   (10 attempts)
2. Medium (7 attempts)
3. Hard   (5 attempts)

Your choice: 1

Great! You chose EASY mode.
You have 10 attempts. Good luck!

Attempt 1/10
Enter your guess (1-100): 40
Too low! Try going a little higher.

Attempt 2/10
Enter your guess (1-100): 75
Too high! Try something lower.

Attempt 3/10
Enter your guess (1-100): 62

You got it! The number was 62.
You figured it out in 3 attempt(s)!

Thanks for playing! See you again.
```

### Example 2: Game Over (Hard Mode)

```text
Choose your difficulty:
1. Easy   (10 attempts)
2. Medium (7 attempts)
3. Hard   (5 attempts)

Your choice: 3

Great! You chose HARD mode.
You have 5 attempts. Good luck!

Attempt 1/5
Enter your guess (1-100): 20
Too low! Try going a little higher.

Attempt 2/5
Enter your guess (1-100): 40
Too low! Try going a little higher.

Attempt 3/5
Enter your guess (1-100): 50
Too low! Try going a little higher.

Attempt 4/5
Enter your guess (1-100): 60
Too low! Try going a little higher.

Attempt 5/5
Enter your guess (1-100): 70
Too low! Try going a little higher.

Out of attempts! Better luck next time.
The secret number was 82.

Thanks for playing! See you again.
```

### Example 3: Invalid Input Handling

```text
Your choice: 5
Hmm, that's not a valid choice. Try again!

Your choice: 2

Great! You chose MEDIUM mode.
You have 7 attempts. Good luck!

Attempt 1/7
Enter your guess (1-100): hello
That's not a valid number. Give it another try!

Enter your guess (1-100): 150
Please enter a number between 1 and 100.

Enter your guess (1-100): 45
Too low! Try going a little higher.
```

---

## Project Structure

```text
number-guessing-game/
│
├── main.py          # Main Python game logic
│
└── README.md        # Project documentation
```

---

## Concepts Used

This project demonstrates several fundamental Python programming concepts:

| Python Concept | Application |
|---|---|
| `random` module | Generates the secret number |
| Dictionaries | Stores difficulty levels and attempt limits |
| Functions | Separates game logic into reusable blocks |
| `while` loops | Repeats input until valid data is received |
| `for` loops | Controls the number of guessing attempts |
| `if-elif-else` | Compares guesses with the secret number |
| Exception Handling | Handles non-numeric input using `try-except` |
| F-strings | Formats dynamic messages |
| `for-else` | Detects when the player runs out of attempts |
| Main Guard | Allows the module to be imported without automatically starting the game |

---

## Future Improvements

Some ideas to make the game even better:

- [ ] Add a Play Again option.
- [ ] Add a scoring system based on difficulty and attempts.
- [ ] Track the player's best score.
- [ ] Add hints such as "Very Close" or "Far Away".
- [ ] Introduce custom number ranges.
- [ ] Add multiplayer functionality.
- [ ] Create a graphical user interface (GUI).

---

## Author

**MOHD YASIR**

Aspiring Python Developer | Computer Science Student

Interested in Python programming, problem-solving, and building practical software projects.


I hope u enjoy this little game...