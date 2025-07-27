from turtle import Turtle

X_START_COORDINATE = 20
MOVE_DISTANCE = 15

class Snake:

    def __init__(self):
        self.snake_body = []
        self.setup_game()
        #self.start_game()

    def setup_game(self):
        x = X_START_COORDINATE
        for i in range(3):
            t = Turtle()
            t.shape("triangle" if i == 0 else "circle")
            t.color("yellow" if i == 0 else "white")
            t.penup()
            t.goto(x, 0)
            x -= 20
            self.snake_body.append(t)
        #s.update()

    def start_game(self):

        for body_num in range(len(self.snake_body)-1, 0, -1):
            x_move = self.snake_body[body_num-1].xcor()
            y_move = self.snake_body[body_num-1].ycor()
            self.snake_body[body_num].goto(x_move, y_move)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].seth(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].seth(270)

    def left(self):
        if self.snake_body[0].heading() != 0: 
            self.snake_body[0].seth(180)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].seth(0)

