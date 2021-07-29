from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.left(180)
        self.penup()

    def spawn_car(self, color, starting_position):
        self.shapesize(stretch_len=random.randint(1, 3))
        self.color(color)
        self.goto(x=random.randint(300, 450), y=random.randint(-starting_position, starting_position))
