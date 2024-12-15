from turtle import Screen
from player import Player
from car import Car
from time import sleep
from game_over import GameOver
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.bgcolor('black')
screen.setup(width = 600, height = 600)
screen.tracer(0)

player = Player()
cars = [Car()]
scoreboard = Scoreboard()

speed = 0.25

screen.listen()
screen.onkey(player.move_up, 'Up')

def move_cars():
    '''
        Call the move() function to move the car objects.
    '''
    for car in cars:
        car.move()

def detect_car_collision():
    '''
        Return false and display game over if the turtle collided with a car, else return true.
    '''
    for car in cars:
        if player.distance(car) < 20:
            game_over = GameOver()
            return False
        
    return True

def remove_outbound_cars():
    '''
        Remove the cars once they have reached the edge of the frame.
    '''
    if cars[0].xcor() < -300:
        cars[0].hideturtle()
        del cars[0]

def detect_wall_collision():
    '''
        Detect if the turtle has reached the top.
    '''
    global speed
    if player.ycor() >= 290:
        sleep(1)
        speed /= 1.5
        player.goto(0, -280)
        scoreboard.update_score()

game_is_on = True
while game_is_on:
    screen.update()

    move_cars()

    if randint(1, 6) % 3 == 0:
        cars.append(Car())

    remove_outbound_cars()
    detect_wall_collision()
    game_is_on = detect_car_collision()

    sleep(speed)

screen.exitonclick()