import turtle

import colorgram
import turtle as t
import random

dot_spacing = 50
dot_size = 20
dot_amount = 10

turt = t.Turtle()
turt.color("tomato")
turt.speed(9)
t.colormode(255)

turt.pensize(dot_size)

# colors = colorgram.extract('hirst_painting.jpg', 30)
#
# rgb_colors = []
#
# for i in colors:
#     r = i.rgb[0]
#     g = i.rgb[1]
#     b = i.rgb[2]
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)


color_list = [(211, 154, 98), (53, 107, 131), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210)]

start_pos = turt.position()

print(start_pos)

turt.up()
home_x = -(dot_spacing*(dot_amount - 1))/2
home_y = -(dot_spacing*(dot_amount - 1))/2

for y in range(dot_amount):
    turt.goto(home_x, home_y + (dot_spacing * y))
    for x in range(dot_amount):
        turt.color(random.choice(color_list))
        turt.setheading(0)
        turt.down()
        turt.forward(0.0001)
        turt.up()
        turt.forward(dot_spacing)

turt.hideturtle()


screen = t.Screen()
screen.exitonclick()

