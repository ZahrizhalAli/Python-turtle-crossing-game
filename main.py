from turtle import Screen
from player import Player
from car_manager import Car
import time
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

player = Player()
car = Car()

is_game_on = True

screen.onkeypress(player.go_forward, "w")

while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()
    for c in car.car_list:
        if player.distance(c) < 20:
            is_game_on = False

    if player.ycor() == 280:
        player.start_again()
        car.increase_level()

screen.exitonclick()