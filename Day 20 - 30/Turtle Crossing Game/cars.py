from turtle import Turtle
import random

#Defining the characterstics of the cars

CAR_COLORS = ["red", "blue", "green", "pink", "orange", "yellow", "purple", "cyan", "magenta", "violet"]

class Cars:

    def __init__(self):
        self.cars_list = []


    def create_cars(self):
        # car_numbers = random.randint(5,30)
        # for _ in range(car_numbers):
        if random.randint(1,20) == 1:
            
            car_length = random.randint(2,5)
            car_starting_position = random.randint(-400, 400)

            new_car = Turtle("square")
            new_car.color(random.choice(CAR_COLORS))
            new_car.shapesize(stretch_len=car_length, stretch_wid=1)
            new_car.penup()
            new_car.goto(400, car_starting_position)
            self.cars_list.append(new_car)

    
    def move_car(self, score):
        car_speed = score * 1.5
        for car in self.cars_list[:]:  # copy of the list
            car.backward(car_speed)
            if car.xcor() < -420:
                car.hideturtle()
                self.cars_list.remove(car)
            elif car.xcor() <= -400:
                car.hideturtle()
                self.cars_list.remove(car)
    

