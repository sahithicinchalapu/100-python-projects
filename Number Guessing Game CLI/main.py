import random


def secret_numf(difficulty):
    if difficulty == 1:
        return random.randint(1, 10)

    elif difficulty == 2:
        return random.randint(1, 50)

    elif difficulty == 3:
        return random.randint(1, 100)

    else:
        print("Please enter the valid input")
        number_guessing_game()
        return None


def attempt_tracker(difficulty):
    attempt_cnt = 1
    secret_num = secret_numf(difficulty)

    if secret_num is None:
        return

    print("Enter the guessed Number :")

    while True:
        try:
            entered_num = int(input(f"Attempt {attempt_cnt} : "))

            if entered_num == secret_num:
                print(f"Yaay !! You Won in {attempt_cnt} attempts :-)")
                break

            elif entered_num < secret_num:
                print("Too Low")

            elif entered_num > secret_num:
                print("Too high")

            attempt_cnt += 1

        except:
            print("Oops! :-(\nEnter a valid number")


    play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again == "y":
        number_guessing_game()
    else:
        print("Thanks for playing :-)")


def number_guessing_game():
    print("Choose the Difficulty level:")
    print("1. Easy (1-10)\n2. Medium (1-50)\n3. Hard (1-100)")

    difficulty = int(input("Enter the difficulty range (1-3): "))
    attempt_tracker(difficulty)


print("Welcome to Number Guessing Game")
number_guessing_game()

