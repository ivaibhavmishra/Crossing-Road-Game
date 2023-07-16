from scoreboard import Scoreboard
from turtle import Screen
from player import Player
from car_manager import Car_Manager
import time
#turtle= Turtle()
screen= Screen()

screen.bgcolor("white")
screen.setup(width=600,height=600)
screen.tracer(0)

player = Player()
screen.listen()
car_manager = Car_Manager()
scoreboard=Scoreboard()
screen.onkey(player.up, "Up")
game_is_on=True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    scoreboard.write_level()
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on= False
            scoreboard.game_end()
            #screen.clear()
    if player.reach_finish_point():

        player.goto_starting_point()
        car_manager.level_up()
        scoreboard.increace_level()


screen.exitonclick()