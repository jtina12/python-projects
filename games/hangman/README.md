# Hangman

Guess the hidden fruit one letter at a time. You get a hint (the first letter and the word length) and `length + 2` chances. Only wrong guesses use up a chance, and the game tells you how long each guess took.

## Run

```bash
python hangman.py
```

## Features

- Random word from a list of fruits
- Input validation (single letters only, no repeated guesses)
- Live progress display such as `_ a _ a _ a`
- Win and lose messages, plus a clean exit with `Ctrl+C`

## Concepts used

`random.choice`, `collections.Counter`, string handling, `time`, loops, `try/except KeyboardInterrupt`.
