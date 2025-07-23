from turtle import Turtle, Screen
import random 
import turtle as tut

# colors = ['red','green','blue','indianred','firebrick','ForestGreen', 'orange', 'yellow', 'cyan']
# directions = [0, 45, 90, 135, 180, 225, 270, 325]

t = Turtle()
print(t)
t.shape("turtle")
t.width(1)
t.speed("fastest")
tut.colormode(255)
i = 0

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for i in range(100):
    i+= 70
    t.setheading(i)
    t.circle(80)
    t.color(random_color())

t.color("cyan")
t.forward(250)
t.left(45)
t.forward(50)
t.circle(50)
t.left(45)
t.forward(50)
t.circle(20)
t.left(45)
t.forward(50)
t.circle(30)
t.left(45)
t.forward(50)
t.circle(35)
t.left(45)
t.forward(50)
t.circle(45)
t.left(35)
display = Screen()
print(display.canvheight)
print(t)
display.exitonclick()


