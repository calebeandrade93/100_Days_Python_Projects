from turtle import Turtle

ALIGN = "center"
MOVE = False
FONT = ("Arial", 25, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.SCORE_PLAYER = 0
        self.SCORE_MACHINE = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(arg=f"{self.SCORE_PLAYER}   {self.SCORE_MACHINE}", align=ALIGN, move=MOVE, font=FONT)

    def increase_pscore(self):
        self.SCORE_PLAYER += 1
        self.clear()
        self.update_score()

    def increase_mscore(self):
        self.SCORE_MACHINE += 1
        self.clear()
        self.update_score()




