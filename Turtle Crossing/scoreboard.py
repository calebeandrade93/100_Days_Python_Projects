from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"
MOVE = False


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.game_level = 15
        self.SCORE = 0
        self.penup()
        self.hideturtle()
        self.goto(-250, 300)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Level: {self.SCORE}", align=ALIGN, move=MOVE, font=FONT)

    def increase_score(self):
        self.game_level_increase()
        self.SCORE += 1
        self.clear()
        self.update_score()

    def game_level_increase(self):
        if self.game_level > 3:
            self.game_level -= 1
        else:
            return self.game_level

    def game_over(self):
        self.goto(0, 0)
        self.pensize(5)
        self.write(arg=f"GAME OVER", align=ALIGN, move=MOVE, font=FONT)
