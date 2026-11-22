def play_21_game():
    current_number = 0
    print("--- Welcome to the 21 Number Game! ---")
    print("Rules: Count 1, 2, or 3 consecutive numbers.")
    print("The player who says '21' loses.\n")

    # Let player choose who starts
    while True:
        choice = input("Do you want to start first? (yes/no): ").strip().lower()
        if choice == "yes":
            turn = "Player"
            break
        elif choice == "no":
            turn = "Computer"
            break
        else:
            print("Please enter 'yes' or 'no'.")

    print(f"\n{turn} starts the game!\n")

    while current_number < 21:
        if turn == "Player":
            print(f"Current count is at: {current_number}")
            try:
                count = int(input("How many numbers do you want to say? (1-3): "))
                if count not in [1, 2, 3]:
                    print("Invalid input! You must choose 1, 2, or 3.")
                    continue
                
                print("Player says:", end=" ")
                for _ in range(count):
                    current_number += 1
                    print(current_number, end=" ")
                    if current_number == 21:
                        print("\n\n--> You said 21! YOU LOSE!")
                        return
                print("\n")
                turn = "Computer"
            except ValueError:
                print("Please enter a valid number.")

        else:
            remainder = current_number % 4
            if remainder == 0:
                comp_choice = 1
            else:
                comp_choice = 4 - remainder
            
            if current_number + comp_choice > 21:
                comp_choice = 21 - current_number

            print("Computer says:", end=" ")
            for _ in range(comp_choice):
                current_number += 1
                print(current_number, end=" ")
                if current_number == 21:
                    print("\n\n--> Computer said 21! COMPUTER LOSES! YOU WIN!")
                    return
            print("\n")
            turn = "Player"

if __name__ == "__main__":
    play_21_game()
