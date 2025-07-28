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


    def food_random(self, snake_body):    
        while True:
            x_random =  random.randint(-400, 400)
            y_random = random.randint(-400, 400)

            overlap = False

            for segment in snake_body:
                if segment.distance(x_random, y_random) < 20:
                    overlap = True
                    break

            if not overlap:    
                self.goto(x_random, y_random)
                break



