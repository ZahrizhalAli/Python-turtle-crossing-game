from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-270, 270)
        self.write(f"Level: {self.score}", align="left", font=("Arial", 20, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 20, "normal"))
