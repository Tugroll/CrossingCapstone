from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.current_level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.current_level += 1
        self.write(f"Level: {self.current_level}", align="center", font=FONT)


    def end_game(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Your Score is {self.current_level}"
                   f"Game OVER", align="center", font=FONT)