from turtle import Screen , Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scorecard
screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800 , height = 600)
screen.title("Pong Game")
screen.tracer(0)

rpaddle = Paddle((350,0))
lpaddle = Paddle((-350,0))
ball = Ball()
score= Scorecard()


screen.listen()

screen.onkeypress(rpaddle.go_up , "Up")
screen.onkeypress(rpaddle.go_down , "Down")
screen.onkeypress(lpaddle.go_up , "w")
screen.onkeypress(lpaddle.go_down , "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect colision:
    if ball.ycor() >=280 or ball.ycor() <=-280 :
        ball.bounce_y()

    # Detect collision with rpaddle
    if ball.distance(rpaddle)  <= 40 and ball.xcor()>320:
        ball.bounce_x()
    # Detect collision with lpaddle
    if ball.distance(lpaddle)  <= 40 and ball.xcor()<-320:
        ball.bounce_x()


    if ball.xcor() > 360 or ball.xcor()< -360:
        if ball.xcor() > 360:
            score.lpoint()
        else:
            score.rpoint()
        score.score_update()
        ball.reset_position()



screen.exitonclick()