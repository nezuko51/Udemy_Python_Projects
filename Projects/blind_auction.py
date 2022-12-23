import sys
import os
import random

# Last update: 12/11/22

# This short Python project is based on the Day 9 Project called the "Blind Auction" from the Udemy course, 100 Days of Code: The Complete Python Pro Bootcamp for 2023
# I've taken liberty of creating this in my own way that I know best, not so much of following the video guide for certain things (for the sake of efficiency)
# This is the final look of a code, I wanted it to be more modular so that the important steps aren't done in a while loop

# The Blind Auction is a fun, short project that allows users to switch between each other to place the highest bid. Each time a new user is added to the bidding list, the console will clear so that the next user cannot see the bid placed by the previous use
# To make this more interesting, I've programmed the project to randomly select different items to bid for (which isnt part of the original Udemy project).

############################################################################################
# Global variables
final_bids = {}  # global variable that holds record of all bidders & their bidding price
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# this function appends name and bidding price to the global variable "final_bids"
def add_bids(name, bid_price):
    final_bids[name] = bid_price
    return


# function to randomly generate a number between 1-5 to return a random item to bid
def select_item(num):  
    match num:
        case 1:
            print("Item on bid: 2 Laker tickets, FRONT ROW!")
            return
        case 2:
            print("Item on bid: 1 Round-trip ticket to LA!")
            return
        case 3:
            print("Item on bid: $500 giftcard for Supreme!")
            return
        case 4:
            print("Item on bid: $1000 giftcard for Gymshark!")
            return
        case 5:
            print("Item on bid: 2-hour drive in a Porsche 911!")
            return
        case _:
            print("Error: Out of bounds")
            return
    
  
# takes in the bidding record list as argument 
# loops through all dictionary entries and compares the price of each bidder
# returns a print statement of who the highest bidder is
def highest_bid(bid_list):
    highest_bid = 0
    winner = ""
    for person in final_bids:
        amount = final_bids[person]
        if(amount > highest_bid):
            highest_bid = amount
            winner = person
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bidding = True  # while silent auction is bidding is running
print(logo)

# Generate random bidding item
random_num = random.randint(1,5)
select_item(random_num)

while (bidding):
    name = input("What is your name?: ")
    bid_price = int(input("What's your bid?: $"))
    add_bids(name, bid_price) # call add_bids to append to final_bids dictionary 
    add_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    
    if add_bidders == "yes":
        os.system('clear') # clear function call on MacOS
        continue
    elif add_bidders == "no":
        bidding = False
        highest_bid(final_bids)  # call highest_bid() to determine the highest bidder
        break
  
##################################################################
# This section is commented out because I just wanted to create a 
#   separate function that creates the dictionary outside the loop
# This while-loop created the final bid dictionary within itself

# bidding = True
# final_bids = {}
# while (bidding):
#   name = input("What is your name?: ")
#   bid_price = int(input("What's your bid?: $"))
#   final_bids[name] = bid_price
  
#   add_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
#   print(final_bids)
#   if add_bidders == "yes":
#     clear()
#     # continue
#   elif add_bidders == "no":
#     bidding = False
#     highest_bid(final_bids)
#     break
##################################################################