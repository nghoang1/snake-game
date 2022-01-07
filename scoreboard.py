from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updateScore()
        self.hideturtle()
    def updateScore(self):
        self.write(f"Score: {self.score}", align="center", font=('Arial', 8, 'normal'))
    def increaseScore(self):
        self.score +=1
        self.clear()
        self.updateScore()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 8, 'normal') )