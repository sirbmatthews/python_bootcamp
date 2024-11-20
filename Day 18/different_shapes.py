from turtle import Screen, Turtle
from random import randint

turt = Turtle()
turt.shape('triangle')
turt.shapesize(0.5, 0.5, 0.5)

screen = Screen()
screen.colormode(255)

def change_colour():
    r, g, b = (randint(0, 255) for _ in range(3))
    turt.color(r, g, b)

def draw_shape(shape_sides):
    change_colour()
    for _ in range(shape_sides):
        turt.forward(100)
        turt.right(360 / shape_sides)

  
for shape_sides in range(3, 11):
    draw_shape(shape_sides)

print(screen.canvheight)
screen.exitonclick()