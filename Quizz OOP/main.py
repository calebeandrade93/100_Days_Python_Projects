from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for index in question_data:
    data_text = index["text"]
    data_answer = index["answer"]
    new_question = Question(data_text, data_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz !")
print(f"Your final score is: {quiz.score}/{quiz.question_number}\n")
