from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for value in question_data:
    question = Question(value["text"], value["answer"])
    question_bank.append(question)

question_br = QuizBrain(question_bank)

while question_br.still_has_questions():
    question_br.next_question()
