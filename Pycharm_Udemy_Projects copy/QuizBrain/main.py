"""The Quiz Brain project is an Intermediate level that emphasizes the practice of OOP (Object-Oriented Programming) from the Udemy course, 100 Days of Code: The Complete Python Pro Bootcamp for 2023.
(The Intermediate level falls through from Day 15 to Day 31 and the Quiz Brain project is from Day 17.)

The goal of this project is to become familiar with learning how to use Python as an OOP tool (creating classes & constructors).
There are several modules created in this project, most of which were done by scratch and through some video guidance.
The only module that was given to start the project was the data.py that contained a list of dictionaries.

How it works:

The Quiz Brain project is a simple game where a user is taken through a series of questions in a while-loop that checks if there are remaining questions in the question_bank.
So while there are questions left in the question_bank, the loop will continue to run until the user answers incorrectly or if the user finishes the whole game
The question_bank list is a restructured version of the original list of dictionaries >>> [{'text': question, 'answer': answer to question}] <<< in the data.py
Question_bank stores the values taken from data.py and stores those values as (key, value) >>> [{'question': 'answer'}] <<< as opposed to the keys being 'text' and 'answer'
The questions are incremented to the next one if the user happens to answer the current question correctly.
The check_answer() method will check the user's answer against the answered stored in the question_bank list which contains a list of strings that are stored as new_question() objects
The score is also tracked as "number of correct answers / total questions answered".
If answered incorrectly, the program will quit and return the final score to the user. """

## import modules/packages
from quiz_brain_art import quiz_brain_logo
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for i in question_data:
    q_data = i["text"]
    a_data = i["answer"]
    new_question = Question(q_data, a_data)

    # new_question object is appended to question bank so each index looks like
    # [question, answer), (question, answer)]
    question_bank.append(new_question)

# checks to see if questions and answers are stored correctly
# for item in question_bank:
#     print(item.text)
#     print(item.answer)

# create Quiz Brain game object
game = QuizBrain(question_bank)
print(f"\n{quiz_brain_logo}")
print(game.print_intro())

while game.still_has_questions():
    if game.next_question() is False:
        print(f"You're final score is {game.score}/{game.question_number}")
        exit(0)

# only prints if user has answered all questions in the question bank correctly
print(f"Great job! You correctly answered all of the questions in the quiz!\nYou're final score is {game.score}/{game.question_number}")



