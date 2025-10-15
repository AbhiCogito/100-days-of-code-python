import os, random
import tkinter as tk
import pandas as pd 

BACKGROUND_COLOR = "#B1DDC6"
rand_index_list = []
rand_index = 0

os.system("clear")
base_dir = os.path.dirname(os.path.abspath(__file__))

#---------- Locating the images -------------------#
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

#-------------Loading the images----------------#
card_back = tk.PhotoImage(file=image_card_back)
card_front = tk.PhotoImage(file=image_card_front)
right = tk.PhotoImage(file=image_right)
wrong = tk.PhotoImage(file=image_wrong)

#------------Placing the canvas using the grid method------------#
canvas.grid(column=0, row=0, padx=10, pady=10)
card_image = canvas.create_image(410, 270, image=card_front)
card_title = canvas.create_text(400, 100, text="", font=("Times New Roman", 42, "italic"))
card_word = canvas.create_text(400, 220, text="", font=("Times New Roman", 72, "italic"))

words_to_learn_file = os.path.join(base_dir, "data", "words_to_learn.csv")

#--------Loading the words file into a data frams----------#
try:
    df = pd.read_csv(words_to_learn_file)
except FileNotFoundError:
    df = pd.read_csv(data)
    df.to_csv(words_to_learn_file, index=False) #Creating a new csv file to keep track of learning
    print("Creating a new Words 2 Learn file")

def correct_word():
    global rand_index, df
    df = df.drop(rand_index)
    df = df.reset_index(drop=True)
    df.to_csv(words_to_learn_file, index=False) #Saving dataframe to a csv whenever a word is marked as known
    print(f"Length of df: {len(df)}")
    display_french_word()

def display_english_word():
    global rand_index, rand_index_list
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="English Word")
    canvas.itemconfig(card_word, text = f"{df.iloc[rand_index]['English']}")
    right_button = tk.Button(root, image=right, command=correct_word)
    wrong_button = tk.Button(root, image=wrong, command=display_french_word)
    canvas.create_window(550, 400, window=right_button)
    canvas.create_window(250, 400, window=wrong_button)


def display_french_word():
    length = len(df)
    global rand_index, rand_index_list

    if length == 0:
        print("Congrats! All the words have been learned.")
        return 

    while rand_index in rand_index_list:
        rand_index = random.randrange(length)

    if rand_index not in rand_index_list:
        rand_index_list.append(rand_index)
        canvas.itemconfig(card_image, image=card_front)
        canvas.itemconfig(card_title, text="French Word")
        canvas.itemconfig(card_word, text = f"{df.iloc[rand_index]['French']}")
        canvas.after(2000, display_english_word)

display_french_word()

root.mainloop()