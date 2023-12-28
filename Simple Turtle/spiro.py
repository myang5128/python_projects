import turtle 
import random

turt = turtle.Turtle()
turt.shape("turtle")
turt.speed("fastest")
turtle.colormode(255)

for i in range(40):
    curColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turt.color(curColor)
    turt.circle(50)
    turt.seth(i*9)

screen = turtle.Screen()
screen.exitonclick()