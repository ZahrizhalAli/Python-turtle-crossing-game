from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_again()
        self.setheading(90)

    def go_forward(self):
        self.forward(10)

    def start_again(self):
        self.goto(0, -280)
