from question_model import Question
from data import question_data

question_bank = []

for value in question_data:
    question = Question(value["text"], value["answer"])
    question_bank.append(question)

print(question_bank)
