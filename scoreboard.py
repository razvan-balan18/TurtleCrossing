from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Score : {self.score}", align="center", font=FONT)

    def increment(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over", align="center", font=FONT)
