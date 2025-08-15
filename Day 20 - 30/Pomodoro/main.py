
import os, math
import tkinter as tk


file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tomato.png")
os.system("clear")

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
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    c.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")
    title.config(text="Pomodoro Timer!!")
    root.after_cancel(TIMER)
    global REPS 
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        title.config(text="Long break of 20 minutes", fg=GREEN)
    elif REPS % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        title.config(text="Short break of 5 minutes", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        title.config(text="Work focus for 25 minutes", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global REPS
    count_minutes = math.floor(count/60)
    count_sec = count % 60

    if count_minutes <10:
        count_minutes = f"0{count_minutes}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    c.itemconfig(timer_text, text=f"{count_minutes} : {count_sec}")
    
    if count >0:
        global TIMER
        TIMER = root.after(1000, countdown, count - 1)
    else:
        if REPS % 2 != 0:
            marks = "✅" * (REPS//2)
            checkmarks.config(text=marks)

        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("PoMoDoRo Timer!!")
root.config(padx=10, pady=10, bg="cyan")

#Using a Canvas so that we can use it to display the image
c = tk.Canvas(root, width=220, height=240,bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file=file_path) #Saving the image
c.create_image(110,120,image=tomato)   #Using the image

title = tk.Label(text="Timer for Pomodoro!", font=FONT_NAME, fg=GREEN, bg=YELLOW)
title.grid(column=1,row=0)

#Using grid to align the elements
c.create_text(110,10,text="Timer", fill=RED, font=(FONT_NAME, 30, "bold"))
timer_text = c.create_text(110, 140, text="00:00", fill="white",font=(FONT_NAME,60,"italic"))
c.create_window(110,80)
c.grid(column=1, row=1) #Placing the canvas on the grid

start_button = tk.Button(root, text="Start", command= start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)
stop_button = tk.Button(root, text="Reset", command=reset_timer, highlightthickness=0)
stop_button.grid(column=2, row=2)
checkmarks = tk.Label(bg=YELLOW)
checkmarks.grid(column=1,row=2)

root.mainloop()

