from turtle import Turtle, Screen
import random

BALL_RADIUS = 10
BALL_MOVEMENT = 3

class Ball:

    def __init__(self):
        self.b = Turtle("circle")
        self.b.color("pink")
        self.b.penup()
        self.b.circle(BALL_RADIUS)
        heading = random.randint(0,360)
        self.b.seth(heading)

    def ball_move(self):
            self.b.forward(BALL_MOVEMENT)

    def reflect_wall(self):
        current_heading = self.b.heading()
        new_heading = 360 - current_heading
        self.b.seth(new_heading)

    def reflect_paddle(self):
        current_heading = self.b.heading()
        new_heading = (180 - current_heading) % 360
        self.b.seth(new_heading)

    
