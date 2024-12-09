from turtle import Screen
from time import sleep
from player import Player
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title('Pong Game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

player_left = Player((-350, 0), is_left=True)
player_right = Player((350, 0), is_left=False)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player_left.move_up, 'w')
screen.onkeypress(player_left.move_down, 's')
screen.onkeypress(player_right.move_up, 'Up')
screen.onkeypress(player_right.move_down, 'Down')

def detect_wall_collision():
    '''
        Bounce back when the ball collides with the upper or bottom wall
    '''
    if ball.ycor() < -280 or ball.ycor() > 280: 
        ball.bounce_y()

def detect_player_collision():
    '''
        Bounce back when the ball collides with the left or right player\n
        Known bug: The ball bounces multiple times when it hits the topmost or bottommost part of the paddle.
    '''
    if (ball.xcor() < -330 and ball.distance(player_left) < 50) or (ball.xcor() > 330 and ball.distance(player_right) < 50):
        ball.bounce_x()

def detect_ball_out_of_bound():
    '''
        Reset the ball position if the ball is out of bound and award the player a point
    '''
    if ball.xcor() > 390:
        scoreboard.left_point()
        ball.reset_position()

    elif ball.xcor() < -390:
        scoreboard.right_point()
        ball.reset_position()

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    detect_wall_collision()
    detect_player_collision()
    detect_ball_out_of_bound()
    sleep(ball.move_speed)

screen.exitonclick()
