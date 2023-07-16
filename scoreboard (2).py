from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220,250)
        self.level=1

    def write_level(self):
        self.write(f"level: {self.level}", align="center", font=("Courier", 24, "normal"))


    def increace_level(self):
        self.level+=1
        self.clear()

    def game_end(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center" , font=("Courier", 24, "normal"))


