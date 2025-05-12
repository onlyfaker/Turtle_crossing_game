import random
from turtle import Turtle

COLORS = ["red","green","blue","red","yellow","black","purple"]
STARTING_MOVE_DISTANCE = 5

class Car(Turtle):
    def __init__(self):
        super(Car, self).__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2.3, stretch_wid=1)
        random_color = random.choice(COLORS)
        self.color(random_color)
        random_y = random.randint(-200,200)
        self.goto(350,random_y)

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x,self.ycor())


