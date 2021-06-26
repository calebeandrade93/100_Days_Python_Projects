from turtle import Turtle

ALIGN = "center"
MOVE = False
FONT = ("Arial", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.SCORE = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(arg=f"Score: {self.SCORE}", align=ALIGN, move=MOVE, font=FONT)

    def increase_score(self):
        self.SCORE += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGN, move=MOVE, font=FONT)