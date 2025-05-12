# TODO - reset car position after level clear
# TODO - create multiple car objects
# TODO - detect collision with cars
# TODO - scoreboard

import time
from turtle import Turtle,Screen
from player import Player
from scoreboard import Scoreboard
from car import Car
screen = Screen()
screen.setup(width=700,height=500)
screen.tracer(0)
screen.title("Turtle crossing")

player = Player()
car = Car()

screen.listen()
screen.onkey(player.move,"Up")

car_speed = 0.1
game_on=True
while game_on:
    time.sleep(car_speed)
    screen.update()
    car.move()
    screen.update()

    if player.ycor()>240:
        car_speed -=0.05

    






screen.exitonclick()
