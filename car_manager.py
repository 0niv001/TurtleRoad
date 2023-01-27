from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#Creates "cars" of different colours
class CarManager:
    def __init__(self):
        self.all_cars = []
        self.new_car()
        self.smd = STARTING_MOVE_DISTANCE

    # creates new cars at random intervals
    def new_car(self):
        chance = random.randint(1, 6)
        if chance % 3 == 0:
            y = random.randint(-200, 250)
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.color(random.choice(COLORS))
            car.penup()
            car.setposition(300, y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.smd)

    # Increases speed of the car
    def diff(self):
        self.smd += MOVE_INCREMENT
