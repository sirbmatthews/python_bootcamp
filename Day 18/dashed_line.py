from turtle import Screen, Turtle

turt = Turtle()
turt.shape('triangle')
turt.shapesize(0.5, 0.5, 0.5)

screen = Screen()

for i in range(1, 50):
    turt.forward(5)
    if  i % 2 == 0: turt.pendown()
    else: turt.penup()

print(screen.canvheight)
screen.exitonclick()