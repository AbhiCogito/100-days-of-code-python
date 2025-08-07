import turtle, os
import pandas as pd 

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blank_states_img.gif")
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "50_states.csv")
score_log = os.path.join(os.path.dirname(os.path.abspath(__file__)), "score.txt")

screen = turtle.Screen()
screen.title("Guess the USA states game")
screen.addshape(file_path) #Installs the new shape
turtle.shape(file_path) #Uses the new shape

data = pd.read_csv(file)
high_score = pd.read_csv(score_log, sep=',')

game_on = True
score = 0
current_high_score = high_score.loc[0, 'score']

def write_state_name(state,x,y):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.write(state, align="center", font=("Arial", 10, "normal"))


while game_on:
    
    answer = screen.textinput(title=f"{score}/50 correct guesses!", prompt="Write the name of a state in USA: ")

    answer_match = data[data["state"].str.lower() == answer.lower()]
    
    if not answer_match.empty:
        x = answer_match["x"].values[0]
        y = answer_match["y"].values[0]
        score += 1
        write_state_name(answer.title(),x,y)

    if score > int(current_high_score):
        with open(score_log, mode="w") as file:
            file.write("score\n")
            file.write(f"{score}")

    if score == 50 or answer == "exit":
        game_on = False


screen.exitonclick()
