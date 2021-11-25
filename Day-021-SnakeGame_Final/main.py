from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.show_score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)

    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.snake_body[1::]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    #if head collides with any segment in the tail:
        #trigger game_over

screen.exitonclick()


#
# if i > 0:
#     if snake_body[i-1].heading() == 0:
#         new_snake.setpos(snake_body[i-1].pos() + (-20, 0))
#     elif snake_body[i-1].heading() == 90:
#         new_snake.setpos(snake_body[i-1].pos() + (0, -20))
#     elif snake_body[i-1].heading() == 180:
#         new_snake.setpos(snake_body[i-1].pos() + (20, 0))
#     elif snake_body[i-1].heading() == 270:
#         new_snake.setpos(snake_body[i-1].pos() + (0, 20))

