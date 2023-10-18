import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


cars = []


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

score = Scoreboard()
player = Player()
car = CarManager()

screen.onkeypress(player.move_player, "Up")
count = 0


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if count == 3:
        new_car = CarManager()
        cars.append(new_car)
        count = 0
    else:
        count += 1
    for car in cars:
        car.move_car()
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False
    if player.ycor() >= 280:
        score.increment()
        player.reset_pos()

    screen.update()


screen.exitonclick()
