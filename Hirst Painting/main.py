import colorgram
from turtle import Turtle, Screen
import random

# Extraindo 8 cores da imagem
colors = colorgram.extract('hirst_painting.jpg', 20)


def picking_color():
    color = random.choice(colors)
    rgb = color.rgb
    return rgb


# Criando meus objetos.
alex = Turtle()
screen = Screen()
screen.colormode(255)
alex.penup()
alex.speed("fastest")

# Pintando o quadro.
for y in range(-300, 300, 50):
    for x in range(-400, 400, 50):
        alex.pencolor(picking_color())
        alex.setpos(x, y)
        alex.dot(20)



screen.exitonclick()
