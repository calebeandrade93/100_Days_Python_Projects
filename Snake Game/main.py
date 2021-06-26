from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from field import Field
import time

# Configurando a tela
screen = Screen()  # Criando o objeto screen
screen.setup(width=700, height=700)  # Dimensão da tela
screen.bgcolor("black")  # Muda a cor do background da tela
screen.title("Snake Game")  # Título da tela
screen.tracer(0)  # Desligando o tracer

# Criando a snake, food e score
snake = Snake()
food = Food()
score = Score()
field = Field()

# Criando controles
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Começando o jogo
game_on = True
while game_on:
    screen.update()  # A cada vez que as 3 peças se moverem, a screen da um update que mostra todas as 3 deslocadas na
    time.sleep(0.1)  # nova posição.
    snake.move_forward()

    # Detectando colisão com a comida
    if snake.snake_head.distance(food) < 15:
        food.food_respawn()
        snake.extend_snake()
        score.increase_score()

    # Detectando colisão com a parede
    if snake.snake_head.xcor() <= - 300 or snake.snake_head.xcor() >= 300:
        game_on = False
        score.game_over()
    elif snake.snake_head.ycor() <= - 300 or snake.snake_head.ycor() >= 300:
        game_on = False
        score.game_over()

    # Detectando colisão com a calda
    for snake_body in snake.corpo_snake[1:]:
        if snake.snake_head.distance(snake_body) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
