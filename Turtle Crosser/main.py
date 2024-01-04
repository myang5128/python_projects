from turtle import Screen
from cars import Cars
from scoreboard import Scoreboard
from player import Player
import time

# init
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("Turtle Crosser")
screen.tracer(0)
game_On = True
cars_List = []

# objects
scoreboard = Scoreboard()
car = Cars()
player = Player()

screen.listen()
screen.onkey(player.up, "w")
screen.onkey(player.down, "s")
screen.onkey(player.right, "d")
screen.onkey(player.left, "a")

# logic
while game_On:
    screen.update()
    time.sleep(0.1)

    car.create()
    car.move(8 + scoreboard.level)

    if player.ycor() > 290:
        scoreboard.next_Level()
        player.reset()

    for cars in car.cars_List:
        if player.distance(cars) < 20:
            scoreboard.game_Over()
            game_On = False


screen.exitonclick()
