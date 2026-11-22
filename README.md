# Python Beginner Projects 🐍

A collection of small command-line games and practice scripts I wrote while learning Python. Each project is a single, runnable file that focuses on core fundamentals: loops, conditions, functions, input validation, and the `random` module.

## 🎮 Games

| Game | What it is | Concepts practised |
|------|-----------|--------------------|
| [Number Guessing Game](games/number-guessing-game) | Pick a range and guess the secret number in a limited number of tries | `random`, `math.log2`, `try/except`, `while ... else` |
| [Hangman](games/hangman) | Guess the hidden fruit one letter at a time | strings, `Counter`, input validation, timing with `time` |
| [Rock Paper Scissors](games/rock-paper-scissors) | Play against the computer, with replay | `random`, `if/elif`, loops |
| [21 Number Game](games/twenty-one-game) | Take turns counting up to 21; whoever says 21 loses. The computer plays a winning strategy | modulo arithmetic, game logic |
| [Word Guessing Game](games/word-guessing-game) | Guess the characters of a hidden hobby word | loops, strings, `random` |

## 📚 Learning basics

Short exercises from my early practice, in [`learning-basics/`](learning-basics):

- `add_two_numbers.py` and `sum_of_two_numbers.py`: several ways to add two numbers (input, functions, `operator`, `lambda`, a class)
- `array_sum.py`: summing a list with a loop and with the built-in `sum()`
- `max_number.py`: `max()`, `if/else` and the ternary operator
- `factorial.py`: factorial with a `for` loop
- `simple_interest.py` and `compound_interest.py`: interest formulas, with and without user input

## ▶️ How to run

You need [Python 3.8+](https://www.python.org/downloads/). Check with:

```bash
python --version
```

Then clone the repo and run any file:

```bash
git clone https://github.com/YOUR-USERNAME/python-beginner-projects.git
cd python-beginner-projects
python games/hangman/hangman.py
```

On macOS/Linux you may need `python3` instead of `python`.

## 🗂️ Project structure

```
python-beginner-projects/
├── games/
│   ├── hangman/
│   ├── number-guessing-game/
│   ├── rock-paper-scissors/
│   ├── twenty-one-game/
│   └── word-guessing-game/
└── learning-basics/
```

## 🌱 What I learned

- Breaking a problem into small steps before writing code
- Validating user input so programs don't crash on bad entries
- Using loops and conditions to control game flow
- Reading and adapting example code, then making it my own

## 🔭 Ideas for improvement

- Add a scoreboard that is saved between games
- Add difficulty levels
- Rebuild a game with a simple graphical interface (e.g. Tkinter)
