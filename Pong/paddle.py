from turtle import Turtle 

Y_MAX = 250
Y_MIN = -250
MOVEFORCE = 40

class Paddle(Turtle):
    
    def __init__(self, location):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(location)
        
    def up(self):
        if self.ycor() < Y_MAX:
            new_y = self.ycor() + MOVEFORCE
            new_pos = (self.xcor(), new_y)
            self.goto(new_pos)
        

    def down(self):
        if self.ycor() > Y_MIN:
            new_y = self.ycor() - MOVEFORCE 
            new_pos = (self.xcor(), new_y)
            self.goto(new_pos)


