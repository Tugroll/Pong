from turtle import Turtle


class Paddle(Turtle):


    def __init__(self, x):
        super().__init__()
        self.player = Turtle()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.width = 200
        self.setposition(x, 0)

    def go_up(self):
        new_ycor = 10 + self.ycor()
        self.goto(self.xcor(), new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 10
        self.goto(self.xcor(), new_ycor)