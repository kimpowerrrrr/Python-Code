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

end_game = False
draw_card = False

computer_cards = []
computer_score = 0
player_cards = []
player_score = 0

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
        
    if ace == True and current_score > 21:
        index = cards_at_hand.index(11)
        cards_at_hand[index] = 1
        current_score = sum(cards_at_hand)    
    
    return current_score

def check_winner(player_score, computer_score):
    if player_score == 0 or player_score > computer_score:
        return "Player wins!"
    elif computer_score == 0 or computer_score > player_score:
        return "Computer wins!"
    elif player_score == computer_score:
        return "Draw!"
        
#1st deal of cards
player_cards = deal_cards(cards_needed = 2)
computer_cards = deal_cards(cards_needed = 2)

#calculate scores for 1st deal
player_score = calculate_score(player_cards)
computer_score = calculate_score(computer_cards)

print(f"player cards: {player_cards}, score: {player_score}")
print(f"computer cards: {computer_cards}, score: {computer_score}")
print(f"{check_winner(player_score, computer_score)}")

draw_card = str(input("Type 'y' to draw another card, type 'n' to pass"))

        

