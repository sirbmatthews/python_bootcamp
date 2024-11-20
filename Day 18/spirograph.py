from turtle import Screen, Turtle
from random import choice, randint

turt = Turtle()
turt.shape('classic')
turt.shapesize(0.5, 0.5, 0.5)
turt.speed('fastest')

screen = Screen()
screen.colormode(255)

def change_colour():
    r, g, b = (randint(0, 255) for _ in range(3))
    turt.color(r, g, b)

def draw_spirograph():
    for i in range(0, 360, 10):
        turt.setheading(i - 360)
        turt.circle(100)
        change_colour()

draw_spirograph()

print(screen.canvheight)
screen.exitonclick()