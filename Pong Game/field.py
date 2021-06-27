from turtle import Turtle


class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 290)
        self.hideturtle()
        self.drawing_field()

    def drawing_field(self):
        self.right(90)
        self.pensize(width= 2)
        for risk in range(8):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)


        self.pencolor("red")
        self.left(90)
        self.forward(380)
        self.pendown()
        self.left(90)
        self.forward(420)
        self.left(90)
        self.forward(760)
        self.left(90)
        self.forward(440)
        self.left(90)
        self.forward(760)
        self.left(90)
        self.forward(20)


