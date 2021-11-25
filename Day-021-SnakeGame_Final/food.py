from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)
        self.color("turquoise")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x_raw = random.randint(-270, 270)
        y_raw = random.randint(-280, 280)

        x_lack = 10 - (x_raw % 10)
        y_lack = 10 - (y_raw % 10)
        random_x = x_raw + x_lack
        random_y = y_raw + y_lack

        self.goto(random_x, random_y)