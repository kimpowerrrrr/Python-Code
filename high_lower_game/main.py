import random
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
    
    score = 0
    print(logo)
    
    character_a =  get_random_character()
    character_b =  get_random_character()  
    compare_list = [character_a, character_b]

    print(f"{compare_list}")

    display_info(compare_list[0])
    print(vs)
    display_info(compare_list[1])

    higher_lower = str(input(f"Who do you think has the more followers? 'A' or 'B'?: "))
    
    if check_answer(higher_lower, character_a, character_b) != 0:
        score += int(check_answer(higher_lower, character_a, character_b))
        return score
    else:
        return "Game over!"

    

print(start_game())





#display initial card


