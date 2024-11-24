from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier New', 12, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.shape('')
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setposition(0, 290)
        self.write(f'Score: {self.score}', align = ALIGNMENT, font = FONT)
    
    def game_over(self):
        self.setposition(0, 0)
        self.write(f'GAME OVER!', align = ALIGNMENT, font = FONT)