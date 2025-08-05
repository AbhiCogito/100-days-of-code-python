from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-50, 350)  # Top-left corner of the screen
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Courier", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "bold"))