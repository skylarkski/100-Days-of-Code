import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

difficulty = 20
car_array = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

scoreboard.show_level()

for i in range(difficulty):
    new_car = CarManager()
    car_array.append(new_car)

screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")

print(player.ycor())

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    for i in car_array:
        i.move()

    for i in car_array:
        if player.distance(i.xcor(), i.ycor()) < 28:
            game_is_on = False


    if player.ycor() > 300:

        #Set player back to start
        player.sety(-280)

        #Increase speed of cars
        for i in car_array:
            i.increase_speed()

        #Show New Scoreboard Level
        scoreboard.increase_level()
        scoreboard.show_level()

scoreboard.show_game_over()

screen.exitonclick()