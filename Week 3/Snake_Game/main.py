from turtle import Screen, Turtle
import time
from Snake import Snake
from Food import Food

s = Screen()
s.setup(width= 1000, height= 1000)
s.bgcolor("black")
s.title("Welcome to the Snake Game!")
s.tracer(0)

snake = Snake()
food = Food()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

game_on = True

while game_on:
    s.update()
    time.sleep(0.1)
    snake.start_game()

    if snake.snake_body[0].distance(food) < 20:
        food.food_random()
        s.update()

    
    

s.exitonclick()