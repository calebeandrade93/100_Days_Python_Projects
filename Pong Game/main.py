from turtle import Screen
from ball import Ball
from paddles import Paddles
from score import ScoreBoard
from field import Field
import time

# Setando a tela
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Criando os objetos
ball = Ball()
right_paddle = Paddles((350, 0))
left_paddle = Paddles((-350, 0))
score_board = ScoreBoard()
field_drawing = Field()


screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
going_up = True
going_down = False


game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move_ball()

    # Detectar colisão do player da direita
    if right_paddle.ycor() >= 180:
        right_paddle.goto(350, 190)
    elif right_paddle.ycor() <= - 170:
        right_paddle.goto(350, - 170)

    # Detectar colisão player esquerda
    if left_paddle.ycor() >= 180:
        left_paddle.goto(-350, 190)
    elif left_paddle.ycor() <= - 170:
        left_paddle.goto(-350, - 170)


    # Detectar colisão com a bola
    if ball.ycor() > 200 or ball.ycor() < - 200:
        ball.fisica_bola_y()

    # Detectar colisão com o machine_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < - 340:
        ball.fisica_bola_x()

    # Detectar se a bola passou do paddle
    if ball.xcor() > 380 or ball.xcor() < - 380:
        if ball.xcor() > 380:
            score_board.increase_pscore()
            ball.reset_ball()
        else:
            score_board.increase_mscore()
            ball.reset_ball()

screen.exitonclick()
