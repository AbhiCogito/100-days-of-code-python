from turtle import Screen
from scoreboard import Scoreboard
from cars import Cars
from player import Player
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCORE = 0

s = Screen()
s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
s.bgcolor("white")
s.title("Turtle Crossing Game!")
s.tracer(0)

car = Cars()
player = Player()
scoreboard = Scoreboard()

s.listen()
s.onkey(player.move_player, "Up")

game_on = True

def collision(player, car):
    car_width = car.shapesize()[1] * 20  # width (x)
    car_height = car.shapesize()[0] * 20  # height (y)

    car_left = car.xcor() - car_width / 2
    car_right = car.xcor() + car_width / 2
    car_top = car.ycor() + car_height / 2
    car_bottom = car.ycor() - car_height / 2

    player_x = player.xcor()
    player_y = player.ycor()

    if car_left < player_x < car_right and car_bottom < player_y < car_top:
        return True
    return False

# def collision(player, car):
#     car_length = car.shapesize()[0] * 20 #Height of car
#     car_width = car.shapesize()[1] * 20 #Width of car

#     car_left = car.xcor() - car_width/2
#     car_bottom = car.ycor() - car_length/2

#     if player.ycor() + 10 > car_left or player.xcor()+10 > car_bottom:
#         return True
#     return False

while game_on:
    car.create_cars()
    car.move_car(SCORE + 1)
    s.update()
    # time.sleep(0.05)

    if player.ycor() > 400:
        scoreboard.increase_score()
        player.reset_player()
        s.update()

    for c in car.cars_list:
        if collision(player, c):
            scoreboard.game_over()
            game_on = False
            break


s.exitonclick()