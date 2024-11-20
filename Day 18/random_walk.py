from turtle import Screen, Turtle
from random import choice, randint

turt = Turtle()
turt.shape('classic')
turt.shapesize(0.5, 0.5, 0.5)
turt.pensize(5)

screen = Screen()
screen.colormode(255)

direction = [0, 90, 180, 270, 360]

def change_colour():
    r, g, b = (randint(0, 255) for _ in range(3))
    turt.color(r, g, b)

def random_walk():
    change_colour()
    turt.forward(25)
    turt.setheading(choice(direction))
    

for _ in range(200):
    random_walk()

print(screen.canvheight)
screen.exitonclick()