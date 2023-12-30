from turtle import Turtle, Screen 

turt = Turtle()
screen = Screen()
    
def turn_right():
    turt.seth(0)
    turt.forward(15)
    
def turn_left():
    turt.seth(180)
    turt.forward(15)
    
def turn_up():
    turt.seth(90)
    turt.forward(15)
    
def turn_down():
    turt.seth(270)
    turt.forward(15)
    
def reset():
    turt.reset()
    turt.home()

screen.listen()
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="w", fun=turn_up)
screen.onkey(key="s", fun=turn_down)
screen.onkey(key="c", fun=reset)
screen.exitonclick()