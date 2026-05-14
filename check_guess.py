def check_guess(user_guess, computer_guess):
    if user_guess > computer_guess:
        print("Try smaller ones.")
        return False
    elif user_guess < computer_guess:
        print("Try greater ones.")
        return False
    else:
        print("YOU GUESSES IT RIGHT !")
        return True
