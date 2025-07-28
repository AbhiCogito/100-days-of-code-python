from turtle import Screen, Turtle
import time
from Snake import Snake
from Food import Food

s = Screen()
s.setup(width= 1100, height= 1100)
s.bgcolor("black")
s.title("Welcome to the Snake Game!")
s.tracer(0)

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(430, 380)
writer.color("white")

def update_score():
    writer.clear()
    writer.write(f"Score = {score}", align="left", font=("Arial", 14, "bold"))


snake = Snake()
food = Food()
score = 0
food.food_random(snake.snake_body)

# Write score at start
writer.write(f"Score = {score}", align="left", font=("Arial", 14, "bold"))

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
    head = snake.snake_body[0]

    if head.distance(food) < 20:
        food.food_random(snake.snake_body)
        score += 1
        snake.increase_length(score)
        s.update()
        update_score()

    if (head.xcor() > 530 or head.xcor() < -530 or
    head.ycor() > 400 or head.ycor() < -400):
        writer.goto(0, 0)
        writer.write(f"Game Over!", align="center", font=("Arial", 14, "bold"))
        game_on = False

    if snake.collission_with_self():
        writer.goto(0, 0)
        writer.write(f"Game Over!", align="center", font=("Arial", 14, "bold"))
        game_on = False


s.exitonclick()