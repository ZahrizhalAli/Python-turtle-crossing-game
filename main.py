from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

player = Player()
car = Car()
score = Scoreboard()

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
            score.game_over()

    if player.ycor() == 280:
        player.start_again()
        car.increase_level()
        score.increase_score()

screen.exitonclick()