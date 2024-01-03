from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 250)
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        score_Text = (f"{self.l_score} | Score | {self.r_score}")
        self.write(score_Text, align=ALIGNMENT, font=FONT)

    def r_point(self):
        self.r_score += 1
        self.update()
        
    def l_point(self):
        self.l_score += 1
        self.update()
        