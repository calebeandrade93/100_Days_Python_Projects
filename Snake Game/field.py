from turtle import Turtle


class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(290, 0)
        self.pendown()
        self.pensize(2)
        self.pencolor("red")
        self.left(90)
        self.forward(285)
        for drawing in range(3):
            self.left(90)
            self.forward(580)

        self.left(90)
        self.forward(295)
