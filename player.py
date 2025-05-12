import turtle
from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVEMENT = 10

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape('turtle')


    def move(self):
        self.forward(MOVEMENT)
