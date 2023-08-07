# Created by Ricardo Lousada
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350,0)
left_paddle = Paddle(-350,0)
game_ball = Ball(0,0)
game_score = Scoreboard()

screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "a")
screen.onkey(left_paddle.down, "z")


game_is_on = True
while game_is_on:
    time.sleep(game_ball.move_speed)
    screen.update()
    game_ball.move()
    # Check if ball hit the top or bottom of the screen
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()
    # Check collision with the right or left paddle
    if game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_x()
    # hit right wall, left player scores
    if game_ball.xcor() > 380:
        game_ball.reset_position()
        game_score.l_player_scores()
        #print("Left player scores")
    # hit left wall
    if game_ball.xcor() < -380:
        game_ball.reset_position()
        game_score.r_player_scores()
        #print("Right player scores")




screen.exitonclick()
