from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def forward():
    t.forward(5)

def backward():
    t.backward(5)

def rotate_clockwise():
    t.right(10)
    # new_heading = t.heading() + 10
    # t.setheading(new_heading)

def rotate_anti_clockwise():
    t.left(10)
    # new_heading = t.heading() - 10
    # t.setheading(new_heading)

def clear_screen():
    t.reset()

s.listen()
s.onkey(forward, "Right")
s.onkey(backward, "Left")
s.onkey(rotate_clockwise, "Up")
s.onkey(rotate_anti_clockwise, "Down")
s.onkey(clear_screen, "/")

s.exitonclick()