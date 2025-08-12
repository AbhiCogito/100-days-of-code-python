
import os, time
from tkinter import *


file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tomato.png")
os.system("clear")

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "calibri"
BG_COLOR = "cyan"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
w = Tk()
w.title("PoMoDoRo Timer!!")
w.config(padx=10, pady=10, bg="cyan")

c = Canvas(width=220, height=240,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file=file_path) #Saving the image
c.create_image(110,120,image=tomato) #Using the image


#Using pack() to align the elements
c.create_text(110,10,text="Timer", fill=RED, font=(FONT_NAME, 30, "bold"))
c.create_text(110, 140, text="00:00", fill="white",font=(FONT_NAME,60,"italic"))
c.create_text(50,200,text="Start")
c.create_text(160,200,text="Stop")
c.create_text(100,200,text="✅")
c.create_window(110,80)
c.pack()

"""
# Using grid() to align the elements
c.grid(column=2,row=2)
t_timer = Label(text="Timer", bg=BG_COLOR,font=(FONT_NAME, 30, "bold"))
t_timer.grid(column=3, row=2)
t_num = Label(text="00:00", bg=BG_COLOR, font=(FONT_NAME, 30, "italic"))
t_num.grid(column=3, row=4)
t_start = Label(text="Start", bg=BG_COLOR, font=(FONT_NAME, 20, "bold"))
t_start.grid(column=2, row=5)
t_stop = Label(text="Stop",bg=BG_COLOR, font=(FONT_NAME, 20, "bold"))
t_stop.grid(column=5, row=5)

"""


w.mainloop()

