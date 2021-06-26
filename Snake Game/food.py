import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.food_respawn()

    def food_respawn(self):
        ran_x = random.randint(-275, 275)
        ran_y = random.randint(-275, 275)
        self.goto(ran_x, ran_y)
