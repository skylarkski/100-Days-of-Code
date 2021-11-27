from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from net import Net
from scoreboard import Scoreboard
import time

WIDTH = 1600
HEIGHT = 900

p1 = Paddle(-780)
p2 = Paddle(780)

ball = Ball()
scoreboard = Scoreboard()

#Screen Setup
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("PONG")
#No screen animations
screen.tracer(0)

#The Net
net = Net()

screen.listen()
screen.onkeypress(p1.up, "w")
screen.onkeypress(p1.down, "s")
screen.onkeypress(p2.up, "Up")
screen.onkeypress(p2.down, "Down")

game_is_on = True
scoreboard.show_score(p1.score, p2.score)
scoreboard.controls()

while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    if ball.ycor() > (HEIGHT/2 - 20) or ball.ycor() < -(HEIGHT/2 - 20):
        ball.bounce_y()

    if ball.distance(p1) < 40 and ball.xcor() > -(WIDTH/2 - 20) or ball.distance(p2) < 40 and ball.xcor() > (WIDTH/2 - 40):
        ball.bounce_x()


    #reset ball
    if ball.xcor() > WIDTH / 2:
        p2.score += 1
        ball.home()
        ball.bounce_x()
        ball.x_move = 5
        scoreboard.update_score(p1.score, p2.score)

    elif ball.xcor() < -(WIDTH / 2):
        p1.score += 1
        ball.home()
        ball.bounce_x()
        ball.x_move = 5
        scoreboard.update_score(p1.score, p2.score)

    if p1.score == 10:
        scoreboard.p1_wins()
        game_is_on = False
    elif p2.score == 10:
        scoreboard.p2_wins()
        game_is_on = False



screen.exitonclick()
