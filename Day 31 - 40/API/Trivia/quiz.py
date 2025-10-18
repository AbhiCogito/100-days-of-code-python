from Question_format import Question
from data import question_data
import os, random

os.system("clear")

question_bank = []

for i in range(len(question_data)):
    question_text = question_data[i]["question"]
    question_answer = question_data[i]["answer"]
    question_new = Question(question_text, question_answer)
    question_bank.append(question_new)

random.shuffle(question_bank)

class Game:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number} - {current_question.text} Is it true or false?")
        self.check(user_answer, current_question.answer)

    def still_playing(self):
        return not self.question_number == len(self.question_list)
    
    def check(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Eureka!!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")


start = Game(question_bank)
while start.still_playing():
    start.next_question()



