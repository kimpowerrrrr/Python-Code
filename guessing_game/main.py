import art
import random

def choose_difficulty(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    
def check_guess(player_guess, guess_number, attempts):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining")
        player_guess = int(input("Make a guess: "))

        if player_guess == guess_number:
            return "You win!"
        else:
            if player_guess > guess_number:
                print("Too high")
            else:
                print("Too low")
            attempts -= 1

            if attempts == 0:
                return f"Game over! You have {attempts} attempts remaining"
            
def start_game():
    attempts = 0
    player_guess = 0
    play_again = True

    while play_again == True:
        print(art.logo)
        print("Welcome to The Number Guessing Game!")
        print("I'm thinking of a number from 1 to 100")

        #generate random number from 1 to 100
        guess_number = random.randrange(1, 100)

        #make the player choose difficulty
        #easy = 10 attempts
        #hard = 5 attempts
        difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
        attempts = choose_difficulty(difficulty)

        print(check_guess(player_guess, guess_number, attempts))
        reset_game = str(input("Do you want to play again? type 'y' for yes and type 'n' for no: "))
        if reset_game.lower() == "n":
            play_again = False

start_game()

    

