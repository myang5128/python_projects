from question import Question
from data import question_data
from quiz_brain import Teacher

question_bank = []

for i in question_data:
    text = i["question"]
    answer = i["correct_answer"]
    quest = Question(text, answer)
    question_bank.append(quest)

quiz = Teacher(question_bank)

while quiz.still_question():
    quiz.next_question()

print(
    f"You completed the quiz with a final score of {quiz.score}/{quiz.question_number}, a {round(quiz.score/quiz.question_number, 2)}!")
