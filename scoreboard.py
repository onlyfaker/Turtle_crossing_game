from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.ht()
        self.goto(-330, 210)
        self.color('black')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Verdana", 14, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()