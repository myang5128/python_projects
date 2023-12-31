from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        self.color("white")
        self.update()

    def update(self):
        score_Text = (f"Score: {self.score}")
        self.write(score_Text, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.score += 1
        self.update()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        