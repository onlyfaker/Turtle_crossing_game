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


screen.listen()
screen.onkey(player.move,"Up")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    






screen.exitonclick()
