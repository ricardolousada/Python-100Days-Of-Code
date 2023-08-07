import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Frog Car Game")
screen.tracer(0)
screen.listen()

my_frog = Player()
my_frog.reset_position()
my_cars = CarManager()
game_score = Scoreboard()


screen.onkey(my_frog.move,"Up")

game_is_on = True

while game_is_on:
    time.sleep(my_frog.speed)
    screen.update()
    my_cars.create_car()
    my_cars.move_cars()

    # Detect collision with a car
    for car in my_cars.cars:
        if car.distance(my_frog) < 20:
            game_is_on = False
            game_score.game_over()

    # Detect successful crossing:
    if my_frog.is_at_finnish_line():
        my_frog.go_to_start()
        game_score.increase_level()







screen.exitonclick()