from turtle import Turtle, Screen
import random

s = Screen()
s.setup(width= 500,height= 550)
s.bgcolor("cyan")
num_input = s.numinput("Welcome to the race", "Enter the number of turtles (max 10): ")
is_race_on = True

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-220, 0)

if num_input is None:
    num_turtles = 5  # Default if Cancel is pressed
else:
    num_turtles = int(num_input)  # Ensure it's an int

def y_positions(num):
    y_axis = 550 - 50
    y_pos = 250
    gap = y_axis/(num - 1)
    y_position = []
    for _ in range(num):
        y_position.append(y_pos)
        y_pos -= gap
    return y_position

colors = ["red", "blue", "yellow", "pink", "purple", "salmon", "brown", "magenta", "maroon", "tan"]
y_position = []
y_position = y_positions(num_turtles)
all_turtles = []

for i in range(num_turtles):
    t = Turtle("turtle")
    t.penup()
    t.color(colors[i])
    t.goto(-230, y_position[i])
    all_turtles.append(t)

print(all_turtles)

choice = s.textinput("Welcome to the Turtles' only race!", "Choose color of your fav turtle?")

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on = False
            winner = turtle.pencolor()

            if choice == winner:
                message = f"You have won. The winner is {winner} colored turtle."
            else:
                message = f"You have lost. Thw winner is {winner} colored turtle."

            writer.write(message, align="left", font=("Arial", 14, "bold"))

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)



s.exitonclick()


