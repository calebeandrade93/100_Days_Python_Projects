from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5)
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        return self.goto(new_x, new_y)

    def fisica_bola_y(self):
        self.y_move *= -1

    def fisica_bola_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.fisica_bola_x()
