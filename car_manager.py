from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()
        self.move_car()

    def create_car(self):
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))
        self.left(180)

    def move_car(self):
        self.goto(self.xcor() - random.randint(2, 20), self.ycor())
