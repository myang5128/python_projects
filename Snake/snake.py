from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():

    def __init__(self):
        self.segs = []
        self.create_snake()
        self.head = self.segs[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_turt = Turtle("square")
        new_turt.up()
        new_turt.color("DarkGreen")
        new_turt.goto(position)
        self.segs.append(new_turt)
    
    def reset(self):
        for seg in self.segs:
            seg.goto(1500, 1500)
        self.segs.clear()
        self.create_snake()
        self.head = self.segs[0]
        
    def extend(self):
        self.add_segment(self.segs[-1].position())

    def move(self):
        for seg_num in range(len(self.segs)-1, 0, -1):
            new_x = self.segs[seg_num - 1].xcor()
            old_y = self.segs[seg_num - 1].ycor()
            self.segs[seg_num].goto(new_x, old_y)
        self.segs[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
