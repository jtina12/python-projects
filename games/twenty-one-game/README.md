# 21 Number Game

You and the computer take turns counting upward from 1. On each turn you say 1, 2 or 3 consecutive numbers. **Whoever says 21 loses.** You choose who starts.

## Run

```bash
python twenty_one_game.py
```

## How the computer plays

The computer uses a simple winning strategy: it tries to finish each of its turns on a multiple of 4 (4, 8, 12, 16, 20), which leaves you forced towards 21. It does this with the remainder from `current_number % 4`.

## Concepts used

Functions, `while` loops, modulo arithmetic, input validation with `try/except`.
