import tkinter as tk
from dotenv import load_dotenv
from Question_format import Question
from data import question_data
import os, random

os.system("clear")
root = tk.Tk()

base_dir = os.path.dirname(os.path.abspath(__file__))
#---------- Locating the images -------------------#
true = os.path.join(base_dir, "true.png")
false = os.path.join(base_dir, "false.png")
background = os.path.join(base_dir, "background.png")

background_image = tk.PhotoImage(file=background)
true_image = tk.PhotoImage(file=true)
false_image = tk.PhotoImage(file=false)

question_bank = []

for i in range(len(question_data)):
    question_text = question_data[i]["question"]
    question_answer = question_data[i]["answer"]
    question_category = question_data[i]["category"]
    question_new = Question(question_category, question_text, question_answer)
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



root.title("Quiz Game")
root.geometry("350x600")

canvas = tk.Canvas(root, height=414, width=300)
canvas.grid(column=0, row=0, padx=10, pady=10)
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(150, 150, text="", width=250, font=("Arial", 30, "italic"), fill="white")
canvas.grid(row=0, column=0)

true_button = tk.Button(image=true_image, highlightthickness=0, command=?)
true_button.grid(row=1, column=0)
false_button = tk.Button(image=false_image, highlightthickness=0, command=?)
false_button.grid(row=1, column=1)

root.mainloop()
