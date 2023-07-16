from turtle import Turtle

starting_point = (0,-280)
ending_point_y = 280
moving_distance= 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto_starting_point()
        self.setheading(90)

    def up(self):
        self.forward(moving_distance)

    def goto_starting_point(self):
        self.goto(starting_point)

    def reach_finish_point(self):
        if self.ycor()>ending_point_y:
            return True
        else :
            return False



