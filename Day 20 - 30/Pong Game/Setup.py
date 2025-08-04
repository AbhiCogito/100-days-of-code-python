from turtle import Screen, Turtle
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
NET_SIZE = 20
PADDLE_COLOR = "white"
PADDLE_LENGTH = 5
PADDLE_STEP = 50

class ScreenSetup:
    def __init__(self):
        self.s = Screen()
        self.s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.s.bgcolor("black")
        self.s.title("The Pong Game")
        self.s.tracer(0)
        self.s.listen()

        self.t = Turtle()
        self.t.penup()
        self.t.seth(270)
        self.t.color("white")
        self.t.hideturtle()
    
    def draw_net(self):
        self.t.goto(0, SCREEN_HEIGHT/2)
        for y in range(int(SCREEN_HEIGHT/2), int(-SCREEN_HEIGHT/2), -50):
            self.t.goto(0, y)
            self.t.pendown()
            self.t.forward(NET_SIZE)
            self.t.penup()
        self.s.update()

    def draw_score(self):
        pass #Will write later

class PaddlesSetup:

    def __init__(self):
        
        self.right_paddle = None
        self.left_paddle = None

    def draw_paddles(self, x, y):

        t = Turtle("square")
        t.color(PADDLE_COLOR)
        t.shapesize(stretch_wid= PADDLE_LENGTH, stretch_len=1)
        t.penup()
        t.goto(x, y)
        return t

    def setup_paddles(self):

        right_x = SCREEN_WIDTH/2 - 50
        left_x = -SCREEN_WIDTH/2 + 50

        self.right_paddle = self.draw_paddles(right_x, 0)
        self.left_paddle = self.draw_paddles(left_x, 0)

    def move_right_up(self):
        if self.right_paddle.ycor() < 350:
            self.right_paddle.sety(self.right_paddle.ycor() + 20)

    def move_right_down(self):
        if self.right_paddle.ycor() > -350:
            self.right_paddle.sety(self.right_paddle.ycor() - 20)

    def move_left_up(self):
        if self.left_paddle.ycor() < 350:
            self.left_paddle.sety(self.left_paddle.ycor() + 20)

    def move_left_down(self):
        if self.left_paddle.ycor() > -350:
            self.left_paddle.sety(self.left_paddle.ycor() - 20)



            

        

