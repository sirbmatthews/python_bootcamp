from turtle import Screen, Turtle
from random import randint

colours = ['black', 'blue', 'green', 'orange', 'purple', 'red', 'yellow']
turtles = []
i = 0

for colour in colours:
    turt = Turtle(shape='turtle')
    turt.color(colour)
    turt.penup()
    turt.setposition(-360.00,  (-135.00 + (45 * i)))
    turtles.append(turt)
    i += 1

screen = Screen()
guess = screen.textinput("Make your bet", "Who will win the race? Enter a colour:").lower()

winner = None

while not winner:
    for turt in turtles:
        turt.forward(randint(1, 50))
        if turt.xcor() >= 360.0:
            winner = turt.color()[0]
            break

if guess == winner:
    print(f' You win. The {winner} turtle is the winner.')
else:
    print(f'You lose. The {winner} turtle is the winner.')

screen.exitonclick()