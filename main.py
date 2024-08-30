from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

my_screen = Screen()

my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.tracer()

player1 = Paddle(350)
player2 = Paddle(-350)
my_ball = Ball()
scoreboard = ScoreBoard()

my_screen.listen()

my_screen.onkeypress(player1.go_up, "Up")
my_screen.onkeypress(player1.go_down, "Down")

my_screen.onkeypress(player2.go_up, "w")
my_screen.onkeypress(player2.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(.01)
    my_screen.update()

    my_ball.ball_moving()

    if my_ball.ycor() > 300 or my_ball.ycor() < -300:
        my_ball.bounce()
    my_ball.detect_paddle(player1, player2)

    if my_ball.xcor() > 380:
        my_ball.check_ball()
        scoreboard.increase_score_l()
    if my_ball.xcor() < -380:
        my_ball.check_ball()
        scoreboard.increase_score_r()

my_screen.exitonclick()
