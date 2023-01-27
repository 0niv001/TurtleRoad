from turtle import Turtle

FONT = ("Courier", 24, "normal")

# Keeps track of user's score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)

    # Adds point
    def point(self):
        self.score += 1
        self.score_update()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=FONT)

    # Updates score on the graphic
    def update(self):
        self.goto(-200, 250)
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)
