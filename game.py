import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            user_guess = int(input("Guess the secret number (1-100): "))
            attempts += 1
            if user_guess < secret_number:
                print("Try a higher number.")
            elif user_guess > secret_number:
                print("Try a lower number.")
            else:
                print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()
