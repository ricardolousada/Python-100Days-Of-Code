import turtle
import turtle as turtle_module
import colorgram
from turtle import Turtle,Screen
import random
"""
colors = colorgram.extract('image.jpg',30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""

list_of_colors = [(188, 19, 46), (244, 233, 61), (252, 230, 236), (217, 238, 244), (195, 76, 34), (218, 66, 106), (15, 142, 89), (196, 176, 19), (21, 125, 173), (108, 182, 209), (18, 167, 213), (209, 153, 90), (26, 40, 75), (36, 43, 110), (79, 175, 96), (181, 44, 65), (235, 231, 5), (216, 67, 48), (217, 129, 153), (125, 185, 119), (238, 161, 180), (8, 61, 38), (148, 209, 221), (9, 92, 53), (6, 87, 109), (160, 30, 27), (237, 169, 162), (159, 212, 183)]
turtle_module.colormode(255)
m_turtle = turtle_module.Turtle()
m_turtle.penup()
m_turtle.hideturtle()
m_turtle.speed("fastest")
m_turtle.setheading(225)
m_turtle.forward(300)
m_turtle.setheading(0)

number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    m_turtle.dot(20,random.choice(list_of_colors))
    m_turtle.forward(50)

    if dot_count % 10 == 0:
        m_turtle.setheading(90)
        m_turtle.forward(50)
        m_turtle.setheading(180)
        m_turtle.forward(500)
        m_turtle.setheading(0)


screen = turtle.Screen()
screen.exitonclick()