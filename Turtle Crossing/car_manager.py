from turtle import Turtle
import random
from scoreboard import Scoreboard
import gc

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
level = Scoreboard()
level.clear()


def random_y():
    rand_y = random.randint(- 250, 250)
    return rand_y


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        dice = random.randint(1, level.game_level)  # Every time a player increase Score, also increase game level
        if level.game_level > 3:
            if dice == 1 or dice == 4:
                new_car = Turtle("square")
                new_car.penup()
                new_car.shape("square")
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.color(random.choice(COLORS))
                new_car.goto(350, random_y())
                self.all_cars.append(new_car)
        else:
            if dice == 1 or dice == 2:
                new_car = Turtle("square")
                new_car.penup()
                new_car.shape("square")
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.color(random.choice(COLORS))
                new_car.goto(350, random_y())
                self.all_cars.append(new_car)

        if len(self.all_cars) > 30:
            self.all_cars.pop(0)
            self.all_cars[0].hideturtle()
            gc.collect()

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

