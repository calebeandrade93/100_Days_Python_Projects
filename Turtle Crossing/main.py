import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setting the Screen
screen = Screen()
screen.setup(width=700, height=700)
screen.tracer(0)

# Setting the objects
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

# Control
screen.listen()
screen.onkeypress(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update()

    # Creating new cars
    car_manager.create_car()

    # Making cars to move
    car_manager.move_cars()

    # Detect collision at starting point
    if player.ycor() <= - 280:
        player.goto(0, - 280)

    # Detect if cross the line
    if player.ycor() >= 280:
        # Score up
        score_board.increase_score()
        # Reset turtle
        player.crossed_line()


    # Detect collision with cars
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
