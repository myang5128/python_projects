from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    with open("Snake\high_score.txt", mode="r") as file:
        HIGH_SCORE = file.read()
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        self.high_Score = self.HIGH_SCORE
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        score_Text = (f"Score: {self.score} | High Score: {self.high_Score}")
        self.write(score_Text, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > int(self.high_Score):
            self.high_Score = self.score
            with open(r"Snake\high_score.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update()
