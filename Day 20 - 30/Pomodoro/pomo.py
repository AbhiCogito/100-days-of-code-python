import os, math
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "calibri"
BG_COLOR = "yellow"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = 0

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tomato.png")
os.system("clear")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        c.itemconfig(title, text="Long break of 20 minutes")

    elif REPS % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        c.itemconfig(title, text="Short break of 5 minutes")

    else:
        countdown(WORK_MIN * 60)
        c.itemconfig(title, text="Work focus for 25 minutes")


# ---------------------------- COUNTDOWN SETUP ------------------------------- #

def countdown(time):
    global TIMER
    minutes = time // 60
    seconds = time % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    if time > 0:
        c.itemconfig(timer_text, text = f"{minutes} : {seconds}")
        print(timer_text, minutes, seconds)
        TIMER = c.after(1000, countdown, time - 1)


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global TIMER, REPS
    c.itemconfig(timer_text, text = "00:00")
    c.after_cancel(TIMER)
    REPS = 0

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("PoMoDoRo Timer!!")
root.config(bg="yellow")
root.geometry("220x240")


c = tk.Canvas(root, width=220, height=240,bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file=file_path) #Saving the image
c.create_image(110,120,image=tomato)   #Using the image in canvas
timer_text = c.create_text(110,130, text="00:00", font=("calibri", 50))
title = c.create_text(110, 100, text="Dynamic Text", fill="black")
start_button = tk.Button(root, text="Start", command=timer)
c.create_window(50, 200, window=start_button) 
reset_button = tk.Button(root, text="Reset", command=reset_timer)
c.create_window(150, 200, window=reset_button)
c.grid(column=0, row=0)

root.mainloop()