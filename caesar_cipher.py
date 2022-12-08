import sys

# This short Python project is based on the Day 8 Project called the "Caesar Cipher" from the Udemy course, 100 Days of Code: The Complete Python Pro Bootcamp for 2023
# I've taken liberty of creating this in my own way that I know best, not so much of following the video guide for certain things (for the sake of efficiency)
# This is the final look of a code broken down into 4 steps

# " The Caesar cipher is based on transposition and involves shifting each letter of the plaintext message by a certain number of letters, historically three, as shown in Figure 5.1. 
# The ciphertext can be decrypted by applying the same number of shifts in the opposite direction. " (https://www.sciencedirect.com/topics/computer-science/caesar-cipher)

# FIXME:fix white space as input...currently cannot do string such as "hello world"...can only take in 1 string, not two
#       will need to split string, encode/decode two strings, join strings back together when returning or printing final 
#       encoded/decoded text

############################################################################################
# Global variables

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#############################################################################################
# def encrypt(plain_text, shift_amount):
#   new_string = ""
#   alph_len = len(alphabet)  # len of alphabet = 26
#   for i in plain_text:
#     orig_pos = alphabet.index(i)
#     new_position = orig_pos + shift_amount
#     # checks if new position after shift 
#     #   is greater than the length opf alphabet

    
#     # if new shift position equals 30, use modulo 
#     #   to loop back to the beginning of the list and continue counting
    
#     # if message = 'hello'
#     # shift = 30
#     # position of letter 'h' = alphabet index 11 which is 'L'

    
#     # so basically ....
#     #   new_position (7 + shift of 30) % length of alphabet (26) = 11
#     # 37 % 26 = 11 --> alphabet[11] = 'L'
#     if(new_position > alph_len):
#       new_letter = alphabet[new_position % alph_len] 
#       new_string += new_letter
#     else:
#       new_letter = alphabet[new_position]
#       new_string += new_letter
#   return "The encoded text is " + new_string

#############################################################################################
# def decrypt(plain_text, shift_amount):
#   new_string = ""
#   alph_len = len(alphabet)  # len of alphabet = 26
#   for i in plain_text:
#     orig_pos = alphabet.index(i)
#     new_position = orig_pos - shift_amount
#      # flip around to traverse the end of list since shift is decreasing in position
#     # instead of new_position % length of alphabet to loop to beginning of list
#     # decoding is the other way around
#     #     -(new_position) % length of alphabet
#     #     (7 index - 17 shift) % 26 = 16 --> "q"
#     if(new_position < 0):
#         new_letter = alphabet[new_position % alph_len]
#         new_string += new_letter
#     else:
#       new_letter = alphabet[new_position]
#       new_string += new_letter
#   return "The decoded text is " + new_string

#############################################################################################
# combined function of both encode and decode running automatically until
#   user specifies to end the program
def caesar(start_text, shift_amount, cipher_direction):
  new_string = ""
  alph_len = len(alphabet)  # len of alphabet = 26
  for i in start_text:
    orig_pos = alphabet.index(i)
    if cipher_direction == "decode":
      new_position = orig_pos - shift_amount
      if (new_position < 0):
        new_letter = alphabet[new_position % alph_len]
        new_string += new_letter
      else:
        new_letter = alphabet[new_position]
        new_string += new_letter
    else:
      new_position = orig_pos + shift_amount
      if(new_position > alph_len):
        new_letter = alphabet[new_position % alph_len]
        new_string += new_letter
      else:
        new_letter = alphabet[new_position]
        new_string += new_letter
  print(f"The {cipher_direction}d text is {new_string}")

############################################################################################
# automated loop for continuous use unless specified otherwise
# FIXME:fix white space as input...currently cannot do string such as "hello world"...can only take in 1 string, not two
#       will need to split string, encode/decode two strings, join strings back together when returning or printing final 
#       encoded/decoded text
run = True
while (run):
  
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  print("\nCURRENT PROGRAM DOES NOT ACCOUNT FOR WHITE SPACE! IT CAN ONLY PROCESS 1 STRING WITH NO SPACES.")
  text = input("\nType your message:\n").lower()
  shift = int(input("\nType the shift number:\n"))
  print("\REMEMBER, SHIFT NUMBER MUST BE THE SAME FOR BOTH ENCODING AND DECODING A MESSAGE!\n")

  caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
 
  end_code = (input("To end, type 'yes'. To continue, type 'no'\n").lower())
  if (end_code == "yes"):
    break
  else:
    continue
      