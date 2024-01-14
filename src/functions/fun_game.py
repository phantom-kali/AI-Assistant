import random
from src.init import tts_instance


def respond(text):
    tts_instance.speak(text)
    print(text)


def play_number_guessing_game(ignore_text):
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    respond("Welcome to the Number Guessing Game!")
    respond("I've selected a random number between 1 and 100. Can you guess it?")

    attempts = 0

    while True:
        user_guess = input("Enter your guess: ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            respond("Please enter a valid number.")
            continue

        attempts += 1

        if user_guess == secret_number:
            respond(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            respond("Too low. Try again.")
        else:
            respond("Too high. Try again.")


if __name__ == "__main__":
    play_number_guessing_game()

