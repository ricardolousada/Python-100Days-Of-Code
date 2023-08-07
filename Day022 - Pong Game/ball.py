from turtle import Turtle

BALL_WIDTH = 1
BALL_HEIGHT = 1
MOVING_SIZE = 20
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


class Ball(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("circle")
        self.shapesize(BALL_HEIGHT, BALL_WIDTH)
        self.color("white")
        self.penup()
        self.goto(x_cor, y_cor)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
