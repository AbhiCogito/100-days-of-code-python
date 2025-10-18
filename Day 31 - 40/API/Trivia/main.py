import tkinter as tk
import requests as rq
import os
from dotenv import load_dotenv

os.system("clear")
root = tk.Tk()

base_dir = os.path.dirname(os.path.abspath(__file__))
#---------- Locating the images -------------------#
kanye = os.path.join(base_dir, "kanye.png")
background = os.path.join(base_dir, "background.png")

kanye_image = tk.PhotoImage(file=kanye)
background_image = tk.PhotoImage(file=background)

def get_quote():
    response = rq.get(url="https://api.kanye.rest")
    response.raise_for_status()

    quote = response.json()['quote']
    canvas.itemconfig(quote_text, text=quote)
    print(quote)


root.title("Kanye: fishsticks")
root.geometry("350x600")

canvas = tk.Canvas(root, height=414, width=300)
canvas.grid(column=0, row=0, padx=10, pady=10)
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(150, 150, text="", width=250, font=("Arial", 30, "italic"), fill="white")
canvas.grid(row=0, column=0)

kanye_button = tk.Button(image=kanye_image, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

root.mainloop()
