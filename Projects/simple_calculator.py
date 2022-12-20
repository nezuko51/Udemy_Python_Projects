import os
import sys

# Last update: 12/20/22

# This short Python project is based on the Day 10 Project called the "Calculator" from the Udemy course, 100 Days of Code: The Complete Python Pro Bootcamp for 2023
# I've taken liberty of personalizing it beyond what is shown in the course and from previous basic experience with Python through self-learning.

# The Simple Calulcator is a basic project that allows the user to run up to 3 input numbers using any kind of operation that's given in the list avaiable to the user 
#   while running the program. The user can choose to continue running the program which will the user to input another number and a new operation. This new number and operation
#   will use the answer from the previous inputs. If the user decides to 'start over' the console will be cleared and the program will restart, otherwise, the user can end the program.
# Additional operations aside from given code in Udemy include: modulo and power (based on Python operators)
#   
#   Example run: 
#    if num1 = 7, num2 = 8 and operation = '*' ----------------> 7 * 8 = 56
#    user = 'continue' --> num3 = 2 and new operation = '+' --> 56 + 2 = 58

############################################################################################
# Global variables
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
  return n1+n2

def subtract(n1, n2):
  return n1 - n2

def divide(n1, n2):
  if (n1 == 0) / n2:
    return "Error: undefined"
  return n1 / n2

def multiply(n1, n2):
  return n1 * n2

def choose_op(operation, num1, num2):
  if operation == "+":
    sum = add(num1, num2)
    return sum
  elif operation == "-":
    diff = subtract(num1, num2)
    return diff
  elif operation == "*":
    product = multiply(num1, num2)
    return product
  elif operation == "/":
    quotient = divide(num1, num2)
    return quotient
  else:
    return 0

operation_symbols = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
end = False

while not(end):
  print(logo)
  print("-----------------------------------")
  num1 = int(input("Enter a number?: "))
  num2 = int(input("Enter another number?: "))
  print("\nList of available operations\n------------------------------")
  for key in operation_symbols:
    print(key)
  operation = input("\nChoose an operation from the line above: ")
  answer = choose_op(operation, num1, num2)
  print(f"\nResult\n-----------\n{num1} {operation} {num2} = {answer}\n")

  keep_running = input("Would you like to start over, continue, or end? Type 'continue' to continue running the current program, 'start over' re-run the program, or 'end' to stop the program: ").lower()
  
  if keep_running == "end":
    end = True
  elif keep_running == "start over":
    os.system('clear')
    continue
  elif keep_running == "continue":
    num3 = int(input("\nWhat is the next number?: "))
    print("\nList of available operations\n------------------------------")
    for key in operation_symbols:
      print(key)
    next_op = input("\nChoose another operation from the line above: ")
    new_answer = choose_op(next_op, answer, num3)
    print(f"\nResult\n-----------\n{answer} {next_op} {num3} = {new_answer}\n")
  #   break
  else:
    print("Invalid input")
    end = True