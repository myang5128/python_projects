from turtle import Turtle
import random

COLOR_LIST = ["red", "blue", "orange", "yellow", "green", "purple"]

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        self.color(random.choice(COLOR_LIST))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)