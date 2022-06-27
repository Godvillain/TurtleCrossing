import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() >= 280:
        scoreboard.update_scoreboard()
        player.starting_position()
        car_manager.increase_speed()

screen.exitonclick()
