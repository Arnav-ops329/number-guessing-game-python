import welcome
import number_generation
import user_input
import check_guess


def play_game():
    welcome.welcome()
    computer_guess = number_generation.veronica_number_guess()
    chances = 0
    won = False
    while chances < 10:
        user_guess = user_input.get_user_input()

        result = check_guess.check_guess(user_guess, computer_guess)
        chances += 1
        if result:
            won = True
            print("YOU WON")
            break
    if not won:
        print("0 CHANCES LEFT, VERONICA WON.")
