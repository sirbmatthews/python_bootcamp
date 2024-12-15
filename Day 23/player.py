from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.shapesize(1)
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        '''
            Move the car by 10 places
        '''
        self.sety(self.ycor() + MOVE_DISTANCE)