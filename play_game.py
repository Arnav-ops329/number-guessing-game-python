import welcome
import number_generation
import user_input
import check_guess


def play_game():
    welcome.welcome()
    computer_guess = number_generation.veronica_number_guess()
    chances = 0
    while chances < 10:
        user_guess = user_input.get_user_input()

        check_guess.check_guess(user_guess, computer_guess)
        chances += 1
    if chances == 10:
        print("0 GUESS LEFT, VERONICA WON")
