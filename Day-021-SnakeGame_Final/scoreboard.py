from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Lato', 16, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color('white')
        self.penup()

    def show_score(self):
        self.sety(270)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)