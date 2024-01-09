import random
import hangman_art
import hangman_words



chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_game = False
player_lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
print(f"{hangman_art.logo}")
while end_game == False:

    print(f"{hangman_art.stages[player_lives]}")

    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print("-------")
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        #print("-------")
        if letter == guess:
            display[position] = letter

    if guess not in display:
        player_lives -= 1

    if ''.join(display) == chosen_word:
        print("You win!")
        end_game = True
    elif player_lives == 0:
        end_game = True
        print(f"{hangman_art.stages[0]}")
        print("Game over! ")

    
    print(f"{display}")
   


print(display)