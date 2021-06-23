from turtle import Turtle, Screen
import random

# Definindo objetos
bag_of_turtles = []
for turtle in range(5):
    turtle = Turtle()
    bag_of_turtles.append(turtle)

screen = Screen()

# Modificando a tela
screen.bgcolor("grey")
screen.setup(width=700, height=500)

# Fazendo a aposta nas tartarugas
user_bet = screen.textinput(title="Faça sua aposta!", prompt="Escolha uma cor: (Red, Blue, Green, Purple, Yellow):").lower()

# Alocando as tartarugas no começo e mudanço suas cores e shapes.
for turtle in bag_of_turtles:
    turtle.shapesize(2)
    turtle.penup()
    turtle.shape("turtle")
    if turtle == bag_of_turtles[0]:
        turtle.color("red")
        turtle.goto(x=-300, y=100)
    elif turtle == bag_of_turtles[1]:
        turtle.color("blue")
        turtle.goto(x=-300, y=200)
    elif turtle == bag_of_turtles[2]:
        turtle.color("green")
        turtle.goto(x=-300, y=0)
    elif turtle == bag_of_turtles[3]:
        turtle.color("purple")
        turtle.goto(x=-300, y=-100)
    else:
        turtle.color("yellow")
        turtle.goto(x=-300, y=-200)

# Função designada para fazer as tartarugas correrem
def race_turtle():
    numero = random.randint(5, 25)
    return numero

# A corrida
turtle_race = True
while turtle_race:
    bag_of_turtles[0].forward(race_turtle())
    bag_of_turtles[1].forward(race_turtle())
    bag_of_turtles[2].forward(race_turtle())
    bag_of_turtles[3].forward(race_turtle())
    bag_of_turtles[4].forward(race_turtle())
    for turtle in bag_of_turtles:
        if turtle.xcor() >= 300:
            turtle_race = False
            turtle_winner = turtle.fillcolor()
            if user_bet == turtle_winner:
                print(f"Parabéns você ganhou ! A tartaruga {turtle_winner} chegou na frente !")
            else:
                print(f"Que pena, a tartaruga {turtle_winner} foi melhor desta vez.")

screen.exitonclick()
