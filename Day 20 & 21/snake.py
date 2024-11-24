from turtle import Turtle
import math
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SNAKE_SEGMENT_SIZE = 20.0
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.snake = []
        self.positions = STARTING_POSITIONS
        self.create_snake()
        self.screen = None

    def create_snake(self):
        '''
            Create inital snake body
        '''
        for position in self.positions:
            new_snake_segment = Turtle(shape='square')
            new_snake_segment.color('white')
            new_snake_segment.penup()
            new_snake_segment.setposition(position)
            self.snake.append(new_snake_segment)
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def check_snake_position(self):
        '''
            Returns the position of the new snake segment
        '''
        if self.tail.heading() == RIGHT: return (self.tail.xcor() - SNAKE_SEGMENT_SIZE, self.tail.ycor())
        elif self.tail.heading() == UP: return (self.tail.xcor(), self.tail.ycor() - SNAKE_SEGMENT_SIZE)
        elif self.tail.heading() == LEFT: return (self.tail.xcor() + SNAKE_SEGMENT_SIZE, self.tail.ycor())
        elif self.tail.heading() == DOWN: return (self.tail.xcor(), self.tail.ycor() + SNAKE_SEGMENT_SIZE)
        
    def create_snake_segment(self):
        '''
            Create a new snake segment
        '''
        new_snake_segment = Turtle(shape='square')
        new_snake_segment.color('white')
        new_snake_segment.penup()
        new_snake_segment.setposition(self.check_snake_position())
        self.snake.append(new_snake_segment)
        self.positions.append(new_snake_segment.position())

    def move(self):
        '''
            Move the snake forward, update the positioning of all the snake segments.
        '''
        self.head.forward(MOVE_DISTANCE)
        self.positions.pop(-1)
        self.positions.insert(0, self.head.position())
        for segment, position in zip(self.snake, self.positions): segment.setposition(position)

    def review_snake_position(self):
        '''
            Sets the position to the multiple of SNAKE_SEGMENT_SIZE
        '''
        position = self.head.position()
        if position[0] % SNAKE_SEGMENT_SIZE != 0 or position[1] % SNAKE_SEGMENT_SIZE != 0:
            position = (float(math.ceil(position[0])), float(math.ceil(position[1])))
            self.head.setposition((position[0] - (position[0] % SNAKE_SEGMENT_SIZE)),(position[1] - (position[1] % SNAKE_SEGMENT_SIZE)))

    def up(self):
        '''
            Change the direction of the snake to face up
        '''
        self.screen.onkey(None, 'Left')
        self.screen.onkey(None, 'Right')
        if self.head.heading() != DOWN: self.head.setheading(UP)

    def down(self):
        '''
            Change the direction of the snake to face down
        '''
        self.screen.onkey(None, 'Left')
        self.screen.onkey(None, 'Right')
        if self.head.heading() != UP: self.head.setheading(DOWN)

    def left(self):
        '''
            Change the direction of the snake to face left
        '''
        self.screen.onkey(None, 'Down')
        self.screen.onkey(None, 'Up')
        if self.head.heading() != RIGHT: self.head.setheading(LEFT)

    def right(self):
        '''
            Change the direction of the snake to face right
        '''
        self.screen.onkey(None, 'Down')
        self.screen.onkey(None, 'Up')
        if self.head.heading() != LEFT: self.head.setheading(RIGHT)

    def head_position(self):
        '''
            return the heading of the head segment
        '''
        return self.head.position()