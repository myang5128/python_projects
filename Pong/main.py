from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_On = True

r_Paddle = Paddle((350, 0))
l_Paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_Paddle.up, "Up")
screen.onkey(r_Paddle.down, "Down")
screen.onkey(l_Paddle.up, "w")
screen.onkey(l_Paddle.down, "s")


while game_On:
    screen.update()
    time.sleep(ball.ballSpeed)
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_Paddle) < 50 and ball.xcor() > 320 or ball.distance(l_Paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()
        
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()
        


screen.exitonclick()
