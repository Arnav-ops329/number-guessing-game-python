def check_guess(user_guess, computer_guess):
    if user_guess > computer_guess:
        print("Try smaller ones.")
    elif user_guess < computer_guess:
        print("Try greater ones.")
    else:
        print("YOU GUESSES IT RIGHT !")
