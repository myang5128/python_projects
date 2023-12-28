import turtle
import random

turt = turtle.Turtle()

turt.shape("turtle")

dir_list = [0, 90, 180, 270]

def draw(num_sides):
    angle = 360/num_sides 
    for _ in range(num_sides):
        turt.forward(100)
        turt.right(angle)
        
# for i in range(3, 10):
#     draw(i)


turt.speed("fastest")
turtle.colormode(255)

for _ in range(50):
    curColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turt.color(curColor)
    turt.seth(random.choice(dir_list))
    turt.forward(25)

screen = turtle.Screen()
screen.exitonclick()