from turtle import Turtle
import random

COLOR_LIST = ["red", "black", "blue", "yellow"]
Y_MIN = -240
Y_MAX = 250
X_LEVEL = 300


class Cars():

    def __init__(self):
        self.cars_List = []

    def create(self):
        random_Car = random.randint(1, 5)
        if random_Car == 3:
            new_Car = Turtle("square")
            new_Car.up()
            new_Car.shapesize(stretch_wid=1, stretch_len=2)
            new_Car.color(random.choice(COLOR_LIST))
            random_Y = random.randint(Y_MIN, Y_MAX)
            random_Position = (X_LEVEL, random_Y)
            new_Car.goto(random_Position)
            self.cars_List.append(new_Car)

    def move(self, force):
        for car in self.cars_List:
            car.back(force)
