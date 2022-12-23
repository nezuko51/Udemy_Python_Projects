# Last update: 12/22/22

# This a Udemy Capstone Project which is one of many bigger projects aside from smaller ones given throughout the Udemy course, 100 Days of Code: The Complete Python Pro Bootcamp for 2023.

# The Capstone Project serves as a "benchmark" project that allows the user to apply what they have learned so far in the course. So far, the course has introduced functions, returning
#   values from functions, while-loops, for-loops, dictionaries, lists, and nested lists/dictionaries. The caveats of the Capstone Project is that the user is given the choice to look
#   at the list of given hints (not shown here) and the number of hints is based on difficulty level. Below is an example of the level of difficulty given by the course. Due to previous
#   experience with Python, I decided to hash out this whole project with only 1 hint, which is understanding the rules of Blackjack.


# Being the first Capstone Project, it is based of the game Blackjack (or also called Blackjack 21). When running the porgram, the user can choose to start a game of blackjack which
#   the opponent is the Computer. If you are not familiar, a game of Blackjack requires two cards from the deck that are randomly chosen for each the user and the Computer. While user 
#   knows both of their own cards, only ONE of the Computer's cards are shown. User must add up the sum of the values of the cards in their hand in order to decide whether or not they want
#   to get another card from the deck. The goal of the game is to stay under or be at the value of 21 to win the game. If the user is tied with the Computer, a new game must be started.
#   Otherwise, if both user and Computer have cards below 21 and user decides to pass their turn on getting another card, highest sum wins the game. When the winner is decided, the user
#   will be asked to start a new game or quit, a new game will clear the console for sake of neatness and readability. Executing multiple new games of Blackjack crowds the console, making
#   it difficult to keep track of the current running game.

# NOTE: This program only allows user to get asked for another card once and the scores are compared for the winner after that one turn (whether user wants another card or not). It also
#           does not take into account the actual probabilities of the deck of cards when a card is removed after each turn (this is advanced for me).



############### Blackjack Project ########################################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules ###############################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


######################### Import packages ################################
import os
import random


######################## Global variables ################################
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


######################## Blackjack code ##################################

def draw_cards(p_cards, c_cards):
  """ Randomly draws new cards for a new game of Blackjack for the user and computer"""
  num_cards = 2
  card_indx = 0
  
  for i in range(0, num_cards):
    card_indx = random.randint(0,12)
    for i in range(0, len(cards)):
      if card_indx == i:
        player_cards.append(cards[i])
        break
  for i in range(0, num_cards):
    card_indx = random.randint(0,12)
    for i in range(0, len(cards)):
      if card_indx == i:
        computer_cards.append(cards[i])
        break
        
  return player_cards, computer_cards
  
def score(p_cards, c_cards):
  """Returns the score of the current deck for the player"""
  p_sum = 0
  c_sum = 0
  
  for i in p_cards:
    p_sum += i
  for i in c_cards:
    c_sum += i
    
  return p_sum, c_sum

def hit(p_cards):
  """ Pass in player's cards to append a new card from the deck 
      which will return the player's new set of cards"""
  new_card_indx = 0
  new_card_indx = random.randint(0,12)

  for i in range(0, len(cards)):
    if new_card_indx == i:
      p_cards.append(cards[i])
      break  
  return p_cards

def compare(p_score, c_score):
  """Returns a statement that determines winner of Blackjack based on the most 
  current score for player and computer"""
  
  if (p_score > 21):
    return "\nYou went over. You lose."
  if ((p_score > 21) and (c_score <= 21)):
    return "\nYou went over. You lose."
  if (p_score <= 21) and (c_score < p_score):
    return "\nYou win! Your cards were higher than the Computer's cards."
  if (c_score > p_score) and (p_score and c_score <= 21):
    return "\nYou lose! Computer's cards were higher than your cards."
  if (p_score == c_score) and (p_score == c_score) <= 21:
    return "\nYou tied with the Computer. Move onto new cards."
  if (p_score == 21 ) and (p_score > c_score):
    return "\nYou hit 21!. You win! Your cards were also higher than the Computer's cards."
  else:
    return "\nYou went over. You lose."

################################## Run Pogram ##################################

play = True
while (play):
  player_cards = []
  computer_cards = []
 
  print(logo)
  print("Blackjack House Cards\n--------------------------\nAce: 11\nJack: 10\nQueen: 10\nKing: 10\nSpades/Hearts/Diamonds/Cloves: 2 - 9\n")  

  if input("\nType 'y' to start a game or type 'n' to quit: "): 
  
    player, computer = draw_cards(player_cards, computer_cards)
    player_score, computer_score = score(player, computer)
    print(f"\nYour cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    next_card = input("\nType 'y' to get another card or type 'n' to pass: ")

    if next_card == 'y':
      player_hit = hit(player)
      # print(player_hit)
      hit_score, next_c_score = score(player_hit, computer)
      print(f"\nYour current hand: {player_hit}, final score: {hit_score}")
      print(f"Computer's hand: {computer_cards}")
      print(compare(hit_score, next_c_score))

    else:
      print(f"\nYour final hand: {player_cards}, final score: {player_score}")
      print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
      print(compare(player_score, computer_score))

  if input("\nWould you like to continue to a new game? Type 'y' to start over or 'n' to quit: ") == 'y':
    os.system('clear')
    
  else:
    os.system('clear')
    play = False
    
