from turtle import Screen, Turtle
from Setup import ScreenSetup, PaddlesSetup
from ball import Ball

game_on = True
screen = ScreenSetup()
paddle = PaddlesSetup()
ball = Ball()

screen.draw_net()
paddle.setup_paddles()

screen.s.update()
screen.s.listen()
screen.s.onkey(paddle.move_right_up, "Up")
screen.s.onkey(paddle.move_right_down, "Down")
screen.s.onkey(paddle.move_left_up, "w")
screen.s.onkey(paddle.move_left_down, "s")

while game_on:

    screen.s.update()
    ball.ball_move()

    if ball.b.ycor() > 420 or ball.b.ycor() < -420:
        ball.reflect_wall()

    if 430 < ball.b.xcor() < 450:
        right_set = paddle.right_paddle.ycor()

        if right_set - 50 < ball.b.ycor() < right_set + 50:
            ball.reflect_paddle()

    if -450 < ball.b.xcor() < -430:
        left_set = paddle.left_paddle.ycor()

        if left_set - 50 < ball.b.ycor() < left_set + 50:
            ball.reflect_paddle()

    if ball.b.xcor() > 480 or ball.b.xcor() < -480:
        game_on = False



screen.s.exitonclick()


