secret_number = 8
guess_limit = 0
guess_count = 0
outOfGuesses = False

def guess_limit(level):
    if level == "Easy":
        guess_limit = 6
        guess_count = 0
        guess_count += 1

    if level == "Medium":
        guess_limit = 4
        guess_count = 0
        guess_count += 1

    if level == "Hard":
        guess_limit = 3
        guess_count = 0
        guess_count += 1

    return guess_limit


while True:
    guess = int(input("Enter guess: "))
    if guess != secret_number:
        print("""
    There are 3 levels;
    Easy: You get a chance to choose a number from 1 to 10 and you have 6 guesses,
    Medium: You get a chance to choose a number from 1 to 20 and you have 3 guesses,
    Hard: You get a chance to choose a number from 1 to 50 and you have 3 guesses.
    """)
        choice = input("Make a choice: ")

        if choice == "Easy":
            input("Enter guess: ")
            guess_limit = 6
            guess_count += 1

            if guess !=secret_number:
                print("That was wrong")
                guess_count = print(f"You have {guess_limit}")

        elif choice == "Medium":
            input("Enter guess: ")
            guess_limit = 4
            guess_count += 1
            if guess !=secret_number:
                print("That was wrong")
                guess_count = print(f"You have {guess_limit}")

        elif choice == "Hard":
            input("Enter guess: ")
            guess_limit = 3
            guess_count += 1
            if guess !=secret_number:
                print("That was wrong")
                guess_count = print(f"You have {guess_limit}")

        elif choice != "Easy" or choice != "Medium" or choice != "Hard":
            print("Invalid selection.")
        elif outOfGuesses:
            outOfGuesses = True
            print("Game over you lose.")
            break
    else:
        print("You are right!")
        break
