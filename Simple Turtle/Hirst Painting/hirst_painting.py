import turtle
import random

turt = turtle.Turtle()
turt.shape("turtle")
turt.speed("fast")
turtle.colormode(255)

screen = turtle.Screen()

color_list = [(233, 222, 92), (211, 158, 105), (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174), 
              (41, 103, 161), (12, 21, 62), (184, 46, 111), (186, 164, 23), (43, 182, 112), (122, 187, 155), 
              (25, 32, 158), (173, 16, 67), (234, 164, 199), (229, 75, 43), (22, 179, 205), (11, 41, 23), 
              (49, 126, 73), (146, 218, 196), (51, 21, 11), (227, 220, 10), (106, 95, 206), (133, 215, 229), 
              (175, 177, 227), (59, 16, 31), (237, 170, 158), (19, 92, 47), (158, 26, 17), (10, 84, 100), 
              (44, 39, 243), (97, 73, 13), (249, 11, 26)]

turt.hideturtle()
turt.up()
turt.seth(225)
turt.forward(300)
turt.seth(0)

for _ in range(8):
    for i in range(10):
        turt.dot(20, random.choice(color_list))
        turt.fd(50)
    turt.seth(180)
    turt.fd(500)
    turt.seth(90)
    turt.fd(50)
    turt.seth(0)


screen.exitonclick()
