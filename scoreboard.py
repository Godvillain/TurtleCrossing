from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.pencolor("black")
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", False, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)


