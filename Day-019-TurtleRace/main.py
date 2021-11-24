from turtle import Turtle, Screen
import random

width = 800
height = 600
turt_list = []

is_race_on = False

screen = Screen()
screen.setup(width=width, height=height)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

left_edge = -(width/2) + 30

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=left_edge, y=(height-(160 * (i+1)))/2)
    turt_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in range(len(turt_list)):
        if turt_list[i].xcor() > (width/2 - 20):
            is_race_on = False
            winning_color = turt_list[i].pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turt_list[i].forward(rand_distance)

screen.exitonclick()
