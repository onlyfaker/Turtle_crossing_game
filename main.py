# TODO/done - reset car position after level clear
# TODO/done - create multiple car objects
# TODO/done - detect collision with cars
# TODO/done - scoreboard

# TODO - fix - turtle not colliding with the cars correctly
import time
from turtle import Turtle,Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
screen = Screen()
screen.setup(width=700,height=500)
screen.tracer(0)
screen.title("Turtle crossing")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    screen.update()

    #detect colllsion
    for car in car_manager.all_cars:
        if player.distance(car)<20:
            game_on=False
            scoreboard.game_over()
    screen.update()

    if player.resetTurtle():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

    screen.update()

screen.exitonclick()
