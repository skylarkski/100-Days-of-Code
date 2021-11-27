from turtle import Turtle
import random


MOVE_DISTANCE = 20
BALL_SPEED = 5
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

rand_angle = random.randint(135, 225)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.seth(rand_angle)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1.1


