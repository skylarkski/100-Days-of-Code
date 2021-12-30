from turtle import Turtle
ALIGNMENT = "center"
ALIGNMENT_LEFT = "left"

FONT = ("Consolas", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.level = 1
        self.goto(-280, 270)

    def show_level(self):

        self.clear()
        self.write(f"Level: {self.level}", move=False, align=ALIGNMENT_LEFT, font=FONT)

    def increase_level(self):
        self.level += 1

    def show_game_over(self):
        self.clear()
        self.home()
        self.write(f"GAME OVER\nHIGH SCORE: {self.level}", move=False, align=ALIGNMENT, font=FONT)