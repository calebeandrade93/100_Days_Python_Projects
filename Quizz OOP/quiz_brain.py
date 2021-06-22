class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} - (True/False) ?  ").title()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, question_answer):
        if user_answer == question_answer:
            self.score += 1
            print("That's correct !")
            return print(f"Your Score: {self.score}\n")
        else:
            print("Not right")
            print(f"Correct Answer: {question_answer}")
            return print(f"Your Score: {self.score}\n")

