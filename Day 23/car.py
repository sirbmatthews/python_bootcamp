from turtle import Turtle
from random import choice, randrange

COLOURS = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", 
    "beige", "bisque", "blue", "blueviolet", 
    "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", 
    "coral", "cornflowerblue", "cyan", "darkblue", "darkcyan", 
    "darkgray", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen", 
    "darkorange", "darkorchid", "darkred", "deeppink", "deepskyblue"
]

class Car(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('square')
        self.color(choice(COLOURS))
        self.shapesize(stretch_wid = 1, stretch_len = 2)
        self.penup()
        self.setheading(180)
        self.goto(300, randrange(-220, 240, 20))

    def move(self):
        '''
            Move the car by 10 places
        '''
        self.setx(self.xcor() - 10)