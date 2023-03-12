# TODO 2: Define Quiz Brain Model

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        ans = input(f"Q.{self.question_number+1}. {self.question_list[self.question_number].text}\
         (True or False)? ").lower()
        self.question_number += 1
