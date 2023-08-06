# Crated By Ricardo Lousada
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
timmy = Turtle()
# colors = ["red", "green", "blue", "coral", "DarkOrange", "SeaGreen", "SlateGray", "DeepSkyBlue"]
direction = [0, 90, 180, 270]

# timmy.color("green")
# timmy.forward(100)
# timmy.width(15)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_shape(number_of_vectors):
    timmy.color(random_color())
    angle = 360 / number_of_vectors
    print(angle)
    for i in range(number_of_vectors):
        timmy.right(angle)
        timmy.forward(100)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

# random walk
"""for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))
# for shape_size in range(3, 10):
#   draw_shape(shape_size)
"""
screen = Screen()
screen.exitonclick()
