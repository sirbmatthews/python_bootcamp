from turtle import Turtle

class Player(Turtle):

    def __init__(self, position, is_left):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len = 1, stretch_wid = 5)
        self.penup()
        self.goto(position)
        self.is_left = is_left
        self.move_distance = 20

    def move_up(self):
        if self.ycor() < 240: 
            self.sety(self.ycor() + self.move_distance)

    def move_down(self):
        if self.ycor() > -240: 
           self.sety(self.ycor() - self.move_distance)