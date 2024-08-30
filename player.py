from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.shapesize(2)
        self.setheading(90)

    def go_up(self):
        self.forward(10)

    def go_down(self):
        self.backward(10)

    def go_left(self):
        self.goto(self.xcor() - 10, self.ycor())

    def go_right(self):
        self.goto(self.xcor() + 10, self.ycor())