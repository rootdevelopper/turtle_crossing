from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    current_level = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-280, y=260)
        self.hideturtle()
        self.write_level()

    def write_level(self):
        self.write(f"Level: {self.current_level}", move=False, align="left", font=("Arial", 28, "normal"))

    def update_level(self):
        self.current_level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=("Arial", 28, "normal"))
