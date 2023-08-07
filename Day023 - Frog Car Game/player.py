from turtle import Turtle
from typing import Tuple

STARTING_POSITION: tuple[int, int] = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("turtle")
        self.setheading(90)
        self.speed = 0.1

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def cross_finnish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.reset_position()
            self.speed *= 0.9
            return True
        return False

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finnish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.reset_position()
