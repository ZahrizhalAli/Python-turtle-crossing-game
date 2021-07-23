from turtle import Turtle
import random

COLORS = ["red", "black", "blue", "yellow", "green", "purple"]


class Car:
    def __init__(self):
        self.car_list = []
        self.level = 5

    def create_cars(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240, 240)
            new_car.goto(300, random_y)
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.backward(self.level)

    def increase_level(self):
        self.level += 2
