from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed_amount = 2
        self.penup()
        self.setposition(0, 0)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.speed(1)

    def ball_moving(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1
        self.speed_amount += .1
        self.speed(self.speed_amount)
        if self.speed_amount > 3:
            self.speed_amount = 3



    def detect_paddle(self, paddle1, paddle2):
        if self.distance(paddle1) < 50 and self.xcor() < 340 or  self.distance(paddle2) < 50 and  self.xcor() < -340:
            self.x_move *= -1

    def check_ball(self):

        self.speed(15)
        self.goto(0, 0)
        self.speed(1)
        self.x_move *= -1




