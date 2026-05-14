import random

print("===== WELCOME TO THE NUMBER GUESSING GAME =====")
input()
print(
    "Veronica(a computer based player) will guess a number between 1-50 and you have to identify the number in a given number of turns.\nyou would have a total of 10 turns.\nShall we start..."
)
input()
print("Alright, Veronica picked the number, try to guess it...")

user_chance = 0
computer_guess = random.randint(1, 50)
while user_chance != 10:
    try:
        user_guess = int(input("ENTER: "))
        if user_guess > computer_guess:
            user_chance += 1
            print("Try Smaller ones.")
        elif user_guess < computer_guess:
            user_chance += 1
            print("Try greater ones.")
        else:
            user_chance += 1
            print(
                f"YOU'VE GUESSES IT RIGHT !, COMPUTER CHOSE {computer_guess}\nTOTAL GUESSES YOU TOOK: {user_chance}"
            )
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
if user_chance == 10:
    print("CHANCES OVER, VERONICA WON...")
