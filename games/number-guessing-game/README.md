# Number Guessing Game

You choose a lower and upper bound, the computer picks a secret number in that range, and you try to guess it. The number of guesses allowed is calculated with the binary-search formula `ceil(log2(range size))`, so a smart player can always win.

## Run

```bash
python number_guessing_game.py
```

## How to play

1. Enter the lower and upper bound (whole numbers, lower < upper).
2. Guess the number. You are told whether your guess is too small or too high.
3. Win by guessing within the allowed number of tries.

## Concepts used

`random.randint`, `math.log2`, `try/except` for invalid input, `while ... else`.
