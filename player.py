import turtle
from turtle import Turtle

STARTING_POSITION = (0,-230)
MOVEMENT = 10

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape('turtle')
        self.goto(STARTING_POSITION)
        self.left(90)


    def move(self):
        self.forward(MOVEMENT)

    def resetTurtle(self):
        pass



