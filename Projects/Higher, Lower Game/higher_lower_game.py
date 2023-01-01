# Last updated: 12/31/22

# This project is based off of the Day 14 Project called "Higher, Lower" frm the Udemy course, 100 Days of Code: The Complete Python Pro Bootcamp for 2023.
# The "Higher, Lower" game essentially asks the user to choose which individual between two randomly generated celebrities (dummy dataset called 'game_data.py') have the higher follower count.  If the user is able to correctly guess, then they recieve a point but if the user is incorrect, the game ends.
# Simple, right? It's a small little project that was given and written on my own.  Earlier projects provided a small, unfinished template of what the code shold look like. Because this is Day 14, the course now demands to attempt these projects without any guidance other than observing how the actual game works before attempting to write the code.

##################################################### ABOUT MY CODE #################################################################
# The main Python file imports two other simple "modules" that were already given, "game_data.py" and "art.py". "game_data.py" only holds a list of dictionaries that contain the necessary information about celebrities such as name, follower count, occupation, and place of residence.
# When the user runs the program, main pretty much calls the function game() where two variables, person A & person B, are generated based on a random index from the dataset. 
# These will act as "person" objects so that all information within the dictionary can be used to create strings in string_repr() using the keys and values.
# A counter is also initialized to keep track of the user's score when the guess is correct (baseline game, further additions can be made)
# The program then goes into a while-loop that asks the user for their guess 'A' or 'B' and if correct, the counter is incremented.
# The interesting part about this game is that when the user guesses correctly, person B then becomes person A and a new person B is generated. 
# Down below within the if-statements in game(), a new_person variable is initialized to generate a new celebrity, then person A = person B, and person_B = new_person. Essentially B becomes A and a new comparison is made by replacing person B only.
####################################################################################################################################### 

# I also took precaution to consider the happenstance that person A is also person B. If this case occurs, a new person B will be generated to avoid this. However, there may be times when Round 1 choices are flip-flopped around in, let's say, Round 2 of guessing.

# NOTE: This program could be improved to either subtract a point when the user makes an incorrect guess and the game can be ended anytime per user request. 
# Another way this could be improved is that the user can be given a choice to start a new game once an incorrect guess has been made. 
# To make it more interesting, the user can make a specified number of wrong guesses (including docking points) before the program ends and then be given a choice to completely end the running program or to start a new game.


########################### TO D0 ##############################
# (1) import necessary packages such as random, os, sys, art, game data
# "dataset" given is a list of dictionaries which will 
# be used to randomly pick out for each game

# (2) 2 comparisons are done which means two random indexes must be pulled
# First figure out accessing specific indexes, keys, and values (from the dictionaries)

#### THOUGHT: IS IT POSSIBLE TO RANDOMLY GENERATE THE SAME NUMBER FOR TWO VARIABLES???? 
# (3) if answer is correct
# "You're right! Current score: xx"
# Must keep track of current score 
# Person B becomes Person A while a new Person B is randomly generated

# (4) if answer is wrong
# "Sorry, that's wrong. Final score: xx"
# Quit program
#################### HIGHER-LOWER CODE ##########################
import os
import sys
import random
import art
from game_data import data



def initialize():
  """Initialize a randomly generated index that is used to determine the value returned from the dataset called 'data'. This will return the selected dictionary in the list."""
  # end at 49 or else index 50 is reached and throws index error 
  # can't do randint(0,50) because there is no index 50
  # check for index through printing
  new_person_index = random.randint(0,49) 
  new_person = data[new_person_index]
  # print(new_person)
  # print(new_person_index)
  
  # print(new_person['name']) # accesses value for key 'name'
  # print(type(new_person['follower_count'])) # check data type for follower count to ensure that number can be compared using logical operators
  
  # print(string_repr(new_person)) # check if string function works 

  return new_person

# create a compare function to compare the number of followers between the chosen people
def comparison(p_A_num, p_B_num):
  """ Compares the follower count between person A and person B"""
#   pass in dictionary VALUE in form of p_A['follower_count']
#    maybe return boolean
  follow_count_A = p_A_num['follower_count']
  follow_count_B = p_B_num['follower_count']
  
  if follow_count_A > follow_count_B: # if A, return True
    return p_A_num
  elif follow_count_A < follow_count_B: # if not A, return False
    return p_B_num
    

# create a string function
def string_repr(person):
  """Returns a string of the randomly generated Instagram account"""
  return f"{person['name']}, a(n) {person['description']}, from {person['country']}."


def game():
  """ A function that runs the 'game'. If user answers correctly, person B becomes person A while a new_person object is created to replace person B for the next round. If user answers incorrectly, the game quits and user is given their final score."""
  # print(len(data)) ## checking for length of dataset for randomization
  p_A = initialize()
  p_B = initialize()
  if p_A == p_B:
    p_B = initialize()
  p_A_string = string_repr(p_A)
  p_B_string = string_repr(p_B)
  print(f"Compare A: {p_A_string}")
  print(art.vs)
  print(f"Against B: {p_B_string}")
  
  score = 0
  
  run = True
  while(run):
     
    compare = comparison(p_A, p_B)
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  
    if user_guess == "A" and compare == p_A:
      score += 1
      os.system('clear')
      print(art.logo)
      print(f"You're right! Current score: {score}")
      
      p_new = initialize()
      p_A = p_B
      p_B = p_new
      p_A_newstring = string_repr(p_A)
      p_B_newstring = string_repr(p_B)
      print(f"Compare A: {p_A_newstring}")
      print(art.vs)
      print(f"Against B: {p_B_newstring}")
     
    elif user_guess == "B" and compare == p_B:
      score += 1
      os.system('clear')
      print(art.logo)
      print(f"You're right! Current score: {score}")
      p_new = initialize()
      p_A = p_B
      p_B = p_new
      p_A_newstring = string_repr(p_A)
      p_B_newstring = string_repr(p_B)
      print(f"Compare A: {p_A_newstring}")
      print(art.vs)
      print(f"Against B: {p_B_newstring}")
    else:
      print(f"\nSorry, that's wrong. Final score: {score}")
      run = False
######################### RUN PROGRAM ##########################   

if __name__ == "__main__":
    print(art.logo)
    game()