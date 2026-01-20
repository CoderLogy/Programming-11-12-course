def reverse_guessing_game():
    print("Welcome to the Reverse Guessing Number Game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")

    low, high = 1, 100
    guesses = 0

    while low <= high:
        guess = (low + high) // 2
        guesses += 1
        print(f"Is your number {guess}?")
        user_response = input("Enter 'h', 'l', or 'c': ").lower()

        if user_response == "h":
            low = guess + 1
        elif user_response == "l":
            high = guess - 1
        elif user_response == "c":
            print(f"Yay! I guessed your number {guess} in {guesses} guesses!")
            break
        else:
            print("Invalid input, please type 'h', 'l', or 'c'.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        reverse_guessing_game()

reverse_guessing_game()
