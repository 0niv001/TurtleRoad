import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# GUI
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

p = Player()
screen.onkey(key="Up", fun=p.move)

scoreboard = Scoreboard()
c = CarManager()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    c.new_car()
    c.move_cars()
    for car in c.all_cars:
        if p.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False
        if p.ycor() > 280:
            scoreboard.point()
            p.go_back()
            c.diff()

screen.exitonclick()
