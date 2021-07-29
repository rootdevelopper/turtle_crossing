from turtle import Turtle
from car import Car
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    cars = []

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def spawn_car(self):
        random_chance = random.randint(0, 6)
        if random_chance == 1:
            new_car = Car()
            new_car.spawn_car(color=random.choice(COLORS), starting_position=250)
            self.cars.append(new_car)

    def get_list_of_cars(self):
        return self.cars
