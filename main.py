import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')

car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.move_cars()
    for running_car in car_manager.get_list_of_cars():
        if running_car.distance(player) < 20:
            game_is_on = False
            screen.bgcolor('grey')
            scoreboard.game_over()
    if player.ycor() > 270:
        scoreboard.update_level()
        player.move_to_start_position()

screen.exitonclick()


