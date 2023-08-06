from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
player_bet = screen.textinput(title="Make your bet", prompt="Which tutle will win the race? Enter a color: ")
print(player_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100,-60,-20,20,60,100]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if player_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == player_bet:
                print(f"You won, the winning turtle is the {winning_color} turtle.")
            else:
                print(f"You lost, the winning turtle is the {winning_color} turtle.")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()
