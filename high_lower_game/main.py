import random, os
from game_data import data
from art import vs, logo

game_data_count = len(data)

def get_random_character():
    random_character = data[random.randrange(1, game_data_count)]
    return random_character

def check_answer(answer, char_a, char_b):
    if (char_a['follower_count'] > char_b['follower_count']) and answer.lower() == "a":
        return 1
    elif (char_a['follower_count'] < char_b['follower_count']) and answer.lower() == "b":
        return 1
    else:
        return 0
    
def display_info(character):
    print(f"{character['name']}, a {character['description']} from {character['country']}")

def start_game():
    os.system('cls')
    score = 0
    game_over = False
    print(logo)
    
    while game_over == False:
        compare_list = []
        if score == 0:
            character_a =  get_random_character()
            character_b =  get_random_character()  
        else:
            character_a = character_b
            character_b = get_random_character()

        #check for same character in match
        while character_a['name'] == character_b['name']:
            if character_a['name'] == character_b['name']:
                character_b = get_random_character
            else:
                continue 

        compare_list = [character_a, character_b]

        display_info(compare_list[0])
        print(vs)
        display_info(compare_list[1])

        #ask the question
        ans = str(input(f"Who do you think has the more followers? 'A' or 'B'?: "))
        
        if check_answer(ans, character_a, character_b) != 0:
            score += int(check_answer(ans, character_a, character_b))
            print(f"Your score: {score}")
        else:
            game_over = True
            print(f"Your score: {score}")
            return "Game Over!"

print(start_game())





#display initial card


