import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from message import Message

# Constants
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
message = Message()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.move()
    if random.randint(0, 5) == 5:
        car_manager.generate_car()

    # Check for end of level
    if (player.ycor() > FINISH_LINE_Y):
        player.reset_position()
        car_manager.speedup()
        scoreboard.level_up()

    # Check for collision with player
    for car in car_manager.cars:
        x_diff = abs(car.xcor() - player.xcor())
        y_diff = abs(car.ycor() - player.ycor())
        if x_diff < 20 and y_diff < 20:
            message.write_message("GAME OVER")
            game_is_on = False

    screen.update()

screen.exitonclick()