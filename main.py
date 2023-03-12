from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for value in question_data:
    question = Question(value["text"], value["answer"])
    question_bank.append(question)

question_br = QuizBrain(question_bank)

question_br.next_question()
