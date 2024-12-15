from turtle import Turtle

class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.write('Game Over!', align='center', font=('courier', 14, 'normal'))