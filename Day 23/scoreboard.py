from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_score()


    def update_score(self):
        '''
            Update the scoreboard by increamenting the level of the game.
        '''
        self.clear()
        self.goto(-280, 280)
        self.score += 1
        self.write(f'Level: {self.score}', align = 'left', font = ('courier', 10, 'normal'))