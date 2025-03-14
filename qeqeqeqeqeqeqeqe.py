import random

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter aa number.")
            

def generate_random_number():
    return random.randint(1,100)

def play_game():
    print("Welcome to the Number Guessing Game!")
    random_number = generate_random_number()
    attempts = 0
    while True:
        guess = get_user_guess()
        attempts += 1
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break