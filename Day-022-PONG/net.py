from turtle import Turtle

HEIGHT = 900


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.pensize(5)
        self.setheading(270)
        self.goto(0, HEIGHT/2)

        while self.ycor() > -(HEIGHT/2):
            self.pendown()
            self.forward(50)
            self.penup()
            self.forward(50)