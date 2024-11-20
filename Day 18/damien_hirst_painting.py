from turtle import Screen, Turtle
from random import choice

colour_pallete = [(1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (70, 70, 45), (185, 190, 201), (126, 225, 231), (88, 49, 45), (61, 65, 66)]

turt = Turtle()
turt.shape('classic')
turt.shapesize(0.5, 0.5, 0.5)
turt.penup()
turt.speed('fastest')

screen = Screen()
screen.colormode(255)

def change_colour():
    rbg = choice(colour_pallete)
    return rbg

for i in range(10):
    turt.setposition(-225.00, (i * 50.0) - 300)
    for _ in range(10):
        turt.pendown()
        turt.dot(20, change_colour())
        turt.penup()
        turt.forward(50)

print(screen.canvheight)
screen.exitonclick()