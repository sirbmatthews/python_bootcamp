from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title('Old Skool Snake Game')
screen.bgcolor('black')
screen.screensize(600, 600)
screen.tracer(0)

snake = Snake()
food = Food(snake.positions)
scoreboard = Scoreboard()
snake.screen = screen
screen.update()

def dectect_food_collision():
    snake.review_snake_position()
    snake_head_position = snake.head_position()    
    food_position = food.position()
    if snake_head_position == food_position:
        snake.create_snake_segment()
        food.create_snake_food(snake.positions)
        scoreboard.increase_score()

def detect_wall_collision():
    return not (abs(snake.head.xcor())> 340 or abs(snake.head.ycor()) > 300)

def detect_tail_collission():
    return not snake.head_position() in snake.positions[1:]

game_is_on = True
while game_is_on:
    
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    snake.move()
    screen.update()
    
    dectect_food_collision()
    game_is_on = detect_wall_collision()
    
    if game_is_on:
        game_is_on = detect_tail_collission()
    
    sleep(0.1)

scoreboard.game_over()

screen.exitonclick()
