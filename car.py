import random
from turtle import Turtle

COLORS = ["red","green","blue","red","yellow","black","purple"]
STARTING_MOVE_DISTANCE = 5

class Car():
    def __init__(self):
        super(Car, self).__init__()
        self.all_cars =[]
        self.move_distance = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance==1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-200, 200)
            new_car.goto(350, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_distance)



