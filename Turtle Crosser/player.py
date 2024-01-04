from turtle import Turtle

MOVEFORCE = 20
START_LOCATION = (0, -290)
Y_MIN = -300
Y_MAX = 310
X_MIN = -300
X_MAX = 300


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.reset()

    def up(self):
        if self.ycor() < Y_MAX:
            self.seth(90)
            self.forward(MOVEFORCE)

    def down(self):
        if self.ycor() > Y_MIN:
            self.seth(270)
            self.forward(MOVEFORCE)

    def left(self):
        if self.xcor() > X_MIN:
            self.seth(180)
            self.forward(MOVEFORCE)

    def right(self):
        if self.xcor() < X_MAX:
            self.seth(0)
            self.forward(MOVEFORCE)

    def reset(self):
        self.seth(90)
        self.goto(START_LOCATION)
