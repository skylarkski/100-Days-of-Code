from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        color_chosen = random.choice(COLORS)
        random_location_x = random.randint(-250, 450)
        random_location_y = random.randint(-250, 260)

        self.shape("square")
        self.seth(90)
        self.shapesize(stretch_len=1, stretch_wid=3)
        self.color(color_chosen)
        self.penup()
        self.goto(random_location_x, random_location_y)
        self.speed("fastest")
        self.x_move = STARTING_MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.ycor())
        if self.xcor() < -360:
            #setting a new location for the car that went past left side of screen
            random_location_y = random.randint(-250, 260)
            new_pos_offset = (random.randint(0, 2) * 10)

            self.setx(320 + new_pos_offset)
            self.sety(random_location_y)


    def increase_speed(self):
        self.x_move += 1
