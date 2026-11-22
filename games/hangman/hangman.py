#Hangman Game
import random
import time
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split()
word = random.choice(someWords)

if __name__ == '__main__':
    print(" Guess the word! HINT: It's a name of a fruit.")
    print(f"Hint: The word starts with '{word[0].upper()}' and has {len(word)} letters.")
    print("_ " * len(word))

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    flag = 0

    try:
        while chances > 0 and flag == 0:
            print()
            print(f"⏳ You have {chances} chances left.")

            start_time = time.time()
            guess = input("Enter a letter to guess: ").lower()
            end_time = time.time()

            print(f"🕒 You took {round(end_time - start_time, 2)} seconds to guess.")

            # Validation
            if not guess.isalpha():
                print("⚠️ Enter only a LETTER.")
                continue
            elif len(guess) > 1:
                print("⚠️ Enter only a SINGLE letter.")
                continue
            elif guess in letterGuessed:
                print("⚠️ You already guessed that letter.")
                continue

            # Correct guess
            if guess in word:
                print("✅ Good job! The letter is in the word.")
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
            else:
                print("❌ Wrong guess!")
                chances -= 1  # decrease only if wrong

            # Display current progress
            current_display = ''
            for char in word:
                if char in letterGuessed:
                    current_display += char + ' '
                else:
                    current_display += '_ '

            print(current_display)

            # Check if the word is fully guessed
            if Counter(letterGuessed) == Counter(word):
                print(f"🎉 The word is: {word}")
                print("👏 Congratulations, You won!")
                flag = 1
                break

        if chances == 0 and flag == 0:
            print("\n💀 You lost! Try again.")
            print(f"The word was '{word}'.")

    except KeyboardInterrupt:
        print("\n👋 Bye! Try again later.")
        exit()

