from turtle import Screen, Turtle
from random import randint

timmy = Turtle()
timmy.shape('turtle')

screen = Screen()
screen.colormode(255)


for i in range(100):
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    steps = 300
    angle = 178
    timmy.right(angle)
    timmy.forward(steps)
    timmy.color(r, b, g)
    
print(screen.canvheight)

screen.exitonclick()