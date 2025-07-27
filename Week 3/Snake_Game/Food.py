import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.food_random()

    def food_random(self):    
        x_random = random.randint(-400, 400)
        y_random = random.randint(-400, 400)
        self.goto(x_random, y_random)
    


