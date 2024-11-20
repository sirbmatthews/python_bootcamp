from turtle import Screen, Turtle

turt = Turtle()
screen = Screen()

def move_forwards():
    turt.forward(10)

def move_backwards():
    turt.backward(10)

def turn_right():
    turt.setheading(turt.heading() + 10)

def turn_left():
    turt.setheading(turt.heading() - 10)

def clear():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()

screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()