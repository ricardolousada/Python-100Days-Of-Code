from turtle import Turtle
PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5
MOVING_SIZE = 20
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

class Paddle(Turtle):

    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(PADDLE_HEIGHT,PADDLE_WIDTH)
        self.color("white")
        self.penup()
        self.goto(x_cor,y_cor)

    def up(self):
        y_position = self.ycor()
        if y_position <= (SCREEN_HEIGHT/2) - 80:
            self.goto(self.xcor(),y_position+MOVING_SIZE)

    def down(self):
        y_position = self.ycor()
        if y_position >= -(SCREEN_HEIGHT / 2) + 80:
            self.goto(self.xcor(),y_position-MOVING_SIZE)