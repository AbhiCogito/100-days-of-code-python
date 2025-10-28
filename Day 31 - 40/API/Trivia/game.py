import tkinter as tk
import requests as rq
import os, html

API = "https://opentdb.com/api.php?amount=10&type=boolean"
score = 0
i = 0

os.system("clear")

root = tk.Tk()

#---------- Locating the images -------------------#
base_dir = os.path.dirname(os.path.abspath(__file__))
true = os.path.join(base_dir, "true.png")
false = os.path.join(base_dir, "false.png")
background = os.path.join(base_dir, "background.png")

#----------- Loading the images -------------------#
background_image = tk.PhotoImage(file=background)
true_image = tk.PhotoImage(file=true)
false_image = tk.PhotoImage(file=false)

#----------- Fetching questions via API -----------#
question_data = []
response = rq.get(url=API)
response.raise_for_status()
data = response.json()
results = data["results"]

for item in results:
    q = item["question"]
    question = html.unescape(q)
    answer = item["correct_answer"]
    c = item["category"]
    category = html.unescape(c)

    question_data.append({
        "question": question,
        "answer": answer,
        "category": category
    })

def display_question():
        global i

        if i < len(question_data):
            question = question_data[i]["question"]
            answer = question_data[i]["answer"]
            category = question_data[i]["category"]
            canvas.itemconfig(category_text, text=category)
            canvas.itemconfig(question_text, text=question)
            canvas.itemconfig(score_text, text=f"Score: {score}")
            canvas.itemconfig(answer_text, text="")
        else:
            canvas.itemconfig(category_text, text="")
            canvas.itemconfig(question_text, text=f"Quiz Finished!\nScore: {score}/10")
            true_button.config(state="disabled")
            false_button.config(state="disabled")

def play_game(user_choice = None):
    global i, score
    
    if i < len(question_data):
        answer = question_data[i]["answer"]
        if user_choice == answer:
            score+=1
            canvas.itemconfig(score_text, text=f"Score: {score}")
            canvas.itemconfig(answer_text, text=answer)
            i+=1
            root.after(1000, display_question)
        else:
            canvas.itemconfig(score_text, text=f"Score: {score}")
            canvas.itemconfig(answer_text, text=answer)
            i+=1
            root.after(1000, display_question)

root.title("Quiz Game")
root.geometry("350x600")

canvas = tk.Canvas(root, height=414, width=300)
canvas.grid(column=0, row=0, padx=10, pady=10)
canvas.create_image(150, 207, image=background_image)
category_text = canvas.create_text(160, 50, text="", width=250, font=("Arial", 30, "italic"), fill="black")
question_text = canvas.create_text(150, 180, text="", width=250, font=("Arial", 22, "italic"), fill="white")
score_text = canvas.create_text(150, 350, text=f"Score: {score}", width=250, font=("Arial", 22, "italic"), fill="black")
answer_text = canvas.create_text(150, 300, text="", width=250, font=("Arial", 22, "italic"), fill="black")
canvas.grid(row=0, column=0)

true_button = tk.Button(image=true_image, highlightthickness=0, command=lambda: play_game("True"))
true_button.grid(row=1, column=0)
false_button = tk.Button(image=false_image, highlightthickness=0, command=lambda: play_game("False"))
false_button.grid(row=1, column=1)

display_question()

root.mainloop()