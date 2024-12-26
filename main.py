## Day 22 Project
from turtle import *
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong") # creates name on the top of the window
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle2.go_up, "Up")
screen.onkey(r_paddle2.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update() # refreshes animations
    time.sleep(ball.move_speed) # slows down refresh
    ball.move()
# TODO 1: Detect Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
# TODO 2: Detect Collision with the paddles:
    if ball.distance(r_paddle2) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
# TODO 3: Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()
    if ball.xcor() == -380:
        ball.reset_position()
        scoreboard.increase_r_score()
screen.exitonclick()