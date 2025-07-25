from turtle import Screen, Turtle
import random, turtle

color_list = [ (23, 16, 94), (232, 43, 6), (153, 14, 30), (41, 181, 158), (127, 253, 206), (237, 71, 166), (209, 179, 208), 
              (246, 218, 21), (40, 133, 242), (246, 218, 5), (207, 148, 178), (126, 155, 204), (106, 189, 174), (224, 134, 117), 
              (81, 87, 136), (150, 64, 75), (209, 87, 66), (49, 44, 100), (244, 168, 154), (175, 184, 222), (111, 9, 23), (179, 30, 10)]

t = Turtle()
turtle.colormode(255)
t.speed("fastest")
t.hideturtle()

def draw_dots(direction):
    t.setpos(0, 0)
    t.setheading(direction)
    for y in range(9):
        for x in range(9):
            t.setpos(x * 20 ,y*-40)
            for _ in range(9):
                t.dot(20, random.choice(color_list))
                t.penup()
                t.forward(40)

for x in range(4):
    draw_dots(x * 90)

display = Screen()
display.exitonclick()



