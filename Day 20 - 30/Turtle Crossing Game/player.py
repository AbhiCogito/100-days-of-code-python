from turtle import Turtle

TURTLE_STEP_SIZE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.seth(90)
        self.penup()
        self.goto(0, -400)

    def move_player(self):
        self.forward(TURTLE_STEP_SIZE)

    def reset_player(self):
        self.goto(0, -400)

    