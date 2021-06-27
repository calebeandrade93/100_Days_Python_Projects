from turtle import Turtle

MACHINE_START = (350, 0)
PLAYER_START = (-350, 0)

class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=4, stretch_len=0.5, outline=1)

    def go_up(self):
        new_y = self.ycor() + 20
        return self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        return self.goto(self.xcor(), new_y)
