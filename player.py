import turtle
from turtle import Turtle

STARTING_POSITION = (0,-230)
MOVEMENT = 10

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape('turtle')
        self.go_to_start()
        self.left(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
    def move(self):
        self.forward(MOVEMENT)

    def resetTurtle(self):
        if self.ycor() > 230:
            return True
        else:
            return False




