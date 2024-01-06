from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align= "center" , font = ("Courier" , 66 ,"normal"))
        self.goto(100, 200)
        self.write(self.rscore, align= "center" , font = ("Courier" , 66 ,"normal"))

    def lpoint(self):
        self.lscore +=1 

    def rpoint(self):
        self.rscore += 1


