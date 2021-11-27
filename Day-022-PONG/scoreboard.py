from turtle import Turtle
ALIGNMENT = "center"
ALIGNMENT_RIGHT = "right"

FONT = ('Consolas', 60, 'bold')
FONT_SMALL = ('Consolas', 10, 'bold')

HEIGHT = 900
WIDTH = 1600


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.sety(HEIGHT/2 - 100)

    def controls(self):
        self.sety(HEIGHT/2 - 100)
        self.write(f"Player 1: w/s\nPlayer 2: up/down", move=False, align=ALIGNMENT, font=FONT_SMALL)

    def show_score(self, p1_score, p2_score):
        self.write(f"{p1_score}    {p2_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self, p1_score, p2_score):
        self.clear()
        self.write(f"{p1_score}    {p2_score}", move=False, align=ALIGNMENT, font=FONT)


    def p1_wins(self):
        self.home()
        self.write(f"GAME OVER. PLAYER 1 WINS!", move=False, align=ALIGNMENT, font=FONT)

    def p2_wins(self):
        self.home()
        self.write(f"GAME OVER. PLAYER 2 WINS! ", move=False, align=ALIGNMENT, font=FONT)