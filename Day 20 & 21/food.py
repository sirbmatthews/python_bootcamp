from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self, positions):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.setposition(self.generate_food_position(positions))

    def generate_food_position(self, positions):
        not_empty_spot = True
        while not_empty_spot:
            x, y = ((randint(-14, 14) * 20.0) for _ in range(2))
            if x % 20 == 0 and y % 20 == 0:
                post = (x, y)
                if post not in positions: return post

    def create_snake_food(self, positions):
        self.setposition(self.generate_food_position(positions))