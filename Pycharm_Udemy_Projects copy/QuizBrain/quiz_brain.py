class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    @staticmethod
    def print_intro():
        return "Welcome to Quiz Brain! You will be answering a series of questions stored in our database. " \
               "\nYou have the option to answer with 'True' or 'False'. " \
               "\nIf you answer incorrectly, the quiz will end and you will have your final score.\nGood luck!\n"

    def still_has_questions(self):
        return self.question_number < len(self.question_list)  # not <= because index is out of range

    def next_question(self):
        current_q_idx = self.question_list[self.question_number]
        self.question_number += 1  # increments to next question before method finishes
        user_input = input(f"Q{self.question_number}: {current_q_idx.text} (True or False)?: ").lower()
        if self.check_answer(user_input, current_q_idx.answer) is False:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("\nYou got it right!")

        else:
            print("\nSorry, that answer is incorrect.")
            print(f"The correct answer was: {correct_answer}")
            print(f"Your current score: {self.score}/{self.question_number}\n")
            return False

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}\n")





