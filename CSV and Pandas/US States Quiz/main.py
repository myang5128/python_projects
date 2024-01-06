import turtle 
import pandas 
import csv 

# sets up screen
image = r"CSV and Pandas\US States Quiz\blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=800, height=550)
turtle.addshape(image)
turtle.shape(image)

# sets up data
data = pandas.read_csv(r"CSV and Pandas\US States Quiz\50_states.csv")
state_list = data.state.to_list()

# sets up state turtles
guessed_states = []

# helper functions
def find(item):
    if item in state_list:
        guessed_states.append(item)
        return True 
    return False

def create_turtle(name, position):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.up()
    new_turtle.goto(position)
    new_turtle.write(name, align="center", font=12)
    

while len(guessed_states) != 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct", prompt="What's a state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(r"CSV and Pandas\US States Quiz\states_to_learn.csv")
        break
    if find(answer_state):
        x_pos = int(data[data.state == answer_state].x.iloc[0])
        y_pos = int(data[data.state == answer_state].y.iloc[0])
        position = (x_pos, y_pos)
        create_turtle(answer_state, position)

screen.exitonclick()