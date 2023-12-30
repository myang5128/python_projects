from turtle import Turtle, Screen
import random

race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: (ROY G BIV)")


y_pos = [-90, -60, -30, 0, 30, 60, 90]
color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle_list = []

for turtle_number in range(0, 7):
    new_turt = Turtle(shape="turtle")
    turtle_list.append(new_turt)
    new_turt.up()
    new_turt.color(color_list[turtle_number])
    new_turt.goto(x=-230, y=y_pos[turtle_number])

if user_bet:
    race_on = True
    
while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet: 
                print(f"You won! The winning turtle is {winner}!")
            else:
                print(f"You lost! The winning turtle is {winner}!")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
