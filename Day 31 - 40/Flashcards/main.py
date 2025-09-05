import os, csv,random
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

game_on = True
os.system("clear")
base_dir = os.path.dirname(os.path.abspath(__file__))

data = os.path.join(base_dir, "data", "french_words.csv")
image_card_back = os.path.join(base_dir, "images", "card_back.png")
image_card_front = os.path.join(base_dir, "images", "card_front.png")
image_right = os.path.join(base_dir, "images", "right.png")
image_wrong = os.path.join(base_dir, "images", "wrong.png")

#-----------Main Window------------#
root = tk.Tk()
root.title("French Words Memory Cards")
root.geometry("830x550")
root.config(bg=BACKGROUND_COLOR)

#-----------Creating the canvas-------------#
canvas = tk.Canvas(root, height=526, width=800, bg=BACKGROUND_COLOR)

#Loading the images
card_back = tk.PhotoImage(file=image_card_back)
card_front = tk.PhotoImage(file=image_card_front)
right = tk.PhotoImage(file=image_right)
wrong = tk.PhotoImage(file=image_wrong)

#Placing the canvas using the grid method
canvas.grid(column=0, row=0, padx=10, pady=10)

#--Loading words-list into a local variable--#
with open(data, "r") as file:
    reader = csv.DictReader(file)
    word_pairs = list(reader) 

def right_word():
    global current_word
    if current_word in word_pairs:
        word_pairs.remove(current_word)

def display_english_word():
    global current_word
    for word in word_pairs:
        if word['French'] == current_word:
            canvas.create_image(410, 270, image=card_back)
            canvas.create_text(400, 200, text=word['English'], font=("Times New Roman", 62, "italic"), anchor="center")
            right_button = tk.Button(root, image=image_right, command=right_word)
            wrong_button = tk.Button(root, image=image_wrong, command=display_english_word)
            right_button.grid(column=2, row=1)
            wrong_button.grid(column=1, row=1)

def display_french_word():
    canvas.create_image(410, 270, image=card_front)
    global current_word
    current_word = random.choice(word_pairs)
    canvas.create_text(400, 200, text=f"{current_word['French']}", font=("Times New Roman", 62, "italic"), anchor="center")


display_english_word()


root.mainloop()