import os
from art import logo
clear = lambda: os.system('cls')

bidders_dictionary = []


def ask_bidders_info():
    another_bidder = True

    while another_bidder == True:
        name = input("What is your name: ")
        amount = input("Enter bid amount: ")
        bidders_dictionary.append(
            {
                "name" : name,
                "amount" : amount
            }
        )
        next_bidder = input("Is there another bidder? Y/N: ")

        if next_bidder.lower() == "y":
            clear()
        else:
            another_bidder = False
            clear()

def find_highest_bidder():
    current_highest_bid = 0
    #record highest bid
    for i in range(0, len(bidders_dictionary)):
        if int(bidders_dictionary[i]['amount']) > current_highest_bid:
            current_highest_bid = int(bidders_dictionary[i]['amount'])
        i += 1

    #find highest bid in dictionary
    for bidder in bidders_dictionary:
        if int(bidder['amount']) == current_highest_bid:
            print(f"The highest bid amount is ${bidder['amount']} from bidder {bidder['name']}")
    
         

print(logo)
ask_bidders_info()
find_highest_bidder()




