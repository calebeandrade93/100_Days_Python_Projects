from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.corpo_snake = []
        self.start_snake()
        self.snake_head = self.corpo_snake[0]

    """Criando posição da snake, setando local de início do game e adicionando novas partes do corpo"""

    def start_snake(self):
        for position in STARTING_POSITION:
            self.add_snake_body(position)

    def add_snake_body(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.shapesize(0.8)
        snake.penup()
        snake.goto(position)
        self.corpo_snake.append(snake)

    def extend_snake(self):
        self.add_snake_body(self.corpo_snake[-1].position())

    """Movimentação das peças da cobra"""

    def move_forward(self):
        for snake in range(len(self.corpo_snake) - 1, 0, -1):
            new_x = self.corpo_snake[
                snake - 1].xcor()  # Nesse for loop, a ultima peça da cobra irá pegar a posição da peça a frente
            new_y = self.corpo_snake[
                snake - 1].ycor()  # e irá ficar em seu lugar, sempre que uma nova peça for adicionada, esse
            self.corpo_snake[snake].goto(new_x,
                                         new_y)  # loop ainda será válido, pois ele pega o len da lista do corpo_snake.

        self.corpo_snake[0].forward(MOVE_DISTANCE)

    """Comandos do keyboard"""

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)  # Norte

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)  # Sul

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)  # Oeste

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)  # Leste
