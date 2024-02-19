############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

draw_card = False


def deal_cards(cards_needed):
    cards_dealt = []

    if cards_needed > 1:
        while cards_needed  > 0:
            current_card = random.randrange(0 , len(cards) - 1)
            cards_dealt.append(cards[current_card])
            cards_needed -= 1

        return cards_dealt
    else:
        current_card = random.randrange(0, len(cards) - 1)
        return cards[current_card]

def calculate_score(cards_at_hand):
    ace = False
    tens = False
    current_score = sum(cards_at_hand)

    if len(cards_at_hand) == 2:
        for value in cards_at_hand:
            if value == 11:
                ace = True
            elif value == 10:
                tens = True

        if ace == True and tens == True:
            current_score = 0
            return current_score
    else:
        if current_score == 21:
            return current_score
        
    if ace == True and current_score > 21:
        index = cards_at_hand.index(11)
        cards_at_hand[index] = 1
        current_score = sum(cards_at_hand)    
    
    return current_score

def check_winner(player_score, computer_score):
    player_score = int(player_score)
    computer_score = int(computer_score)
    if player_score == 0 or player_score > computer_score or (player_score <= 21 and computer_score > 21):
        return "Player wins!"
    elif computer_score == 0 or computer_score > player_score or (player_score > 21 and computer_score <= 21):
        return "Computer wins!"
    elif player_score == computer_score:
        return "Draw!"
    
def start_game():  
    continue_game_player = True
    continue_game_computer = True 
    
    computer_cards = []
    computer_score = 0
    player_cards = []
    player_score = 0  

    #1st deal of cards
    player_cards = deal_cards(cards_needed = 2)
    computer_cards = deal_cards(cards_needed = 2)

    #calculate scores for 1st deal
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"player cards: {player_cards}, score: {player_score}")
    print(f"computer cards: [{computer_cards[0]}]")

    if player_score == 0:
        continue_game_player = False
        continue_game_computer = False
        print("Blackjack! Player wins!")
        return
    elif computer_score == 0:
        continue_game_player = False
        continue_game_computer = False
        print("Blackjack! Computer wins!")
        return

    #draw cards for player
    while continue_game_player == True:
        draw_card_player = str(input("Type 'y' to draw another card, type 'n' to pass: "))
        if draw_card_player.lower() == "y":
            player_cards.append(deal_cards(cards_needed= 1))

            #calculate scores
            player_score = calculate_score(player_cards)
            print(f"player cards: {player_cards}, score: {player_score}")
            print(f"computer cards: {computer_cards[0]}")
            continue_game_player = True

        else:
            continue_game_player = False
            print(f"player cards: {player_cards}, score: {player_score}")

    #draw cards for computer
    while continue_game_computer == True:
        if computer_score < 17:
            computer_cards.append(deal_cards(cards_needed= 1))
            computer_score = calculate_score(computer_cards)
            continue_game_computer = True
        else:
            continue_game_computer = False

    print(f"computer cards: {computer_cards}, score: {computer_score}")
    print(f"{check_winner(player_score, computer_score)}")

start_game()