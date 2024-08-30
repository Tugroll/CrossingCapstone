import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
counter = 0

my_scoreboard = Scoreboard()
my_turtle = Player()
my_cars = CarManager()

screen.listen()
screen.onkeypress(my_turtle.go_up, "Up")
screen.onkeypress(my_turtle.go_down, "Down")
screen.onkeypress(my_turtle.go_left, "Left")
screen.onkeypress(my_turtle.go_right, "Right")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    my_cars.create_car()
    my_cars.move_car()

    for car in my_cars.all_cars:
        if car.distance(my_turtle) < 30:
            my_scoreboard.end_game()
            game_is_on = False

    if my_turtle.ycor() == 260:
        my_turtle.goto(0, -280)
        my_scoreboard.update_scoreboard()
        my_cars.increase_speed()
        my_cars.reset_position()

screen.exitonclick()
