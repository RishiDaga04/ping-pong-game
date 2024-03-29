from turtle import Turtle

class Paddle(Turtle):

    def __init__(self , position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1 ,stretch_wid=5) 
        self.penup()
        self.goto(position)
    
    def go_up(self):
        y_new = 20 + self.ycor()
        self.goto(self.xcor() , y_new)
    def go_down(self):
        y_new = -20 + self.ycor()
        self.goto(self.xcor() , y_new)
    