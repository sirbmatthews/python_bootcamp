from turtle import Turtle

class Ball(Turtle):
    '''
        Inherits the Turtle class and creates a ball object for the Pong game.\n
        Contains the move() to move the ball, bounce_y() to bounce the ball against the wall, bounce_x() to bounce against the player and reset_position() to reset the position of the ball.
    '''

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_y = 10 
        self.move_x = 10
        self.move_speed = 0.1

    def move(self):
        self.setx(self.xcor() + self.move_x)
        self.sety(self.ycor() + self.move_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1