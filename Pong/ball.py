from turtle import Turtle
import random

COLOR_LIST = ["red", "blue", "orange", "yellow", "green", "purple"]
X_FORCE = 10
Y_FORCE = 10
START_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(random.choice(COLOR_LIST))
        self.up()
        self.x_move = X_FORCE
        self.y_move = Y_FORCE
        self.ballSpeed = START_SPEED
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        
    def reset(self):
        self.goto(0, 0)
        self.ballSpeed = START_SPEED
        self.color(random.choice(COLOR_LIST))
        self.bounce_x()
        
    def increase_speed(self):
        self.ballSpeed *= 0.9