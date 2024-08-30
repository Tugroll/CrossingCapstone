from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVEMENT_INCREMENT = .1


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            rnd = random.randint(-200, 200)
            new_car.goto(300, rnd - STARTING_MOVE_DISTANCE)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)



    def reset_position(self):
        for car in self.all_cars:
            car.clear()


    def increase_speed(self):
        for car in self.all_cars:

            self.car_speed += MOVEMENT_INCREMENT

            car.backward(self.car_speed)