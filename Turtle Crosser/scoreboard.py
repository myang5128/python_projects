from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
POSITION = (-200, 250)
OVER_POSITION = (0, 0)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(POSITION)
        self.level = 1
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        score_Text = (f"Level: {self.level}")
        self.write(score_Text, align=ALIGNMENT, font=FONT)

    def next_Level(self):
        self.level += 1
        self.update()

    def game_Over(self):
        self.goto(OVER_POSITION)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
