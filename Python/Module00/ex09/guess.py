import random


def guess():
    num = random.randint(1, 99)
    attempts = 0

    print("""
    This is an interactive guessing game!
    You have to enter a number between 1 and 99 to find out the secret number.
    Type 'exit' to end the game.
    Good luck!
    """)

    while 42:
        guess = input("What's your guess between 1 and 99?\n>> ")

        if guess.lower() == 'exit':
            print("Goodbye!")
            return

        if not guess.isdigit():
            print("That's not a number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == num:
            if num == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if attempts == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print(f"Congratulations, you've got it!\nYou won in {attempts} attempts!")
            return
        elif guess < num:
            print("Too low!")
        else:
            print("Too high!")


if __name__ == "__main__":
    guess()
