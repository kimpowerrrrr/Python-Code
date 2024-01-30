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

comp_hand = []
comp_score = 0
comp_deal = False

player_deal = False
player_hand = []
player_score = 0

continue_game = True

#deal cards
def deal_cards(cards_needed):
    #print(cards_needed)
    cards_dealt = []
    if cards_needed > 1:
        while cards_needed > 0:
            current_card = random.randrange(0, len(cards) - 1)
            cards_dealt.append(cards[current_card])
            #print(f"current card being dealt: {cards[current_card]}")
            cards_needed -= 1
        
        return cards_dealt
    else:
        current_card= random.randrange(0, len(cards) - 1)
        return cards[current_card]

def get_score(card_hand):
    current_score = 0
    for value in card_hand:
        current_score += value
    return current_score

def find_winner(comp_score, player_score):
    if comp_score > player_score:
        return "You lose!"
    elif comp_score == player_score:
        return "Draw!"
    else:
        return "You win!"
  
#1st deal
#deal first 2 cards to the player
player_hand = deal_cards(cards_needed=2)
player_score = get_score(player_hand) 

print(f"Your cards are: {player_hand}, your current score is: {player_score}")

#deal first 2 cards to the computer
comp_hand = deal_cards(cards_needed=2)
print(f"Computer's first card: {comp_hand[0]}")

#ask player if will continue for another card
while continue_game == True:
    player_continue = str(input("Type 'y' to get another card, type 'n' to pass: "))
    if player_continue.lower() == "y":
        player_hand.append(deal_cards(cards_needed=1))
        player_score = get_score(player_hand)
        print(f"Your cards are: {player_hand}, your current score is: {player_score}")
        continue_game = True
    else:
        continue_game = False
        player_score = get_score(player_hand)
        comp_score = get_score(comp_hand)
        print(f"player score: {player_score}")
        print(f"computer score: {comp_score}")
        print(f"{find_winner(comp_score, player_score)}")
