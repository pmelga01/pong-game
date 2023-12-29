from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

def screen_setup():
    screen = Screen()
    screen.bgcolor("#65743a")
    screen.setup(width=1200, height=600)
    screen.title("Pong")
    screen.tracer(0)
    return screen

def center_line_setup(thickness):
    # center dashed line
    center_line = Turtle()
    center_line.color("white")
    center_line.hideturtle()
    center_line.penup()
    center_line.speed("fastest")
    center_line.goto(0, 300)
    center_line.setheading(270)
    center_line.pensize(thickness)
    for _ in range(15):
        center_line.pendown()
        center_line.forward(20)
        center_line.penup()
        center_line.forward(20)
    return center_line

# initial setup of screen
screen = screen_setup()

# setup board
score = Score()
center_line = center_line_setup(4) # center dashed line
gameOver = False;
player_1 = Paddle((-550, 0))
player_2 = Paddle((550, 0))
ball = Ball()

screen.listen()

ball.reset_position()

while (not gameOver):
    screen.update()
    time.sleep(0.1)

    if (score.p1_score == 1 or score.p2_score == 1):
        gameOver = True
        score.game_over()
        break

    ball.move()

    # Detect collision with wall (top /  bottom)
    if (ball.ball.ycor() > 280 or ball.ball.ycor() < -280):
        ball.bounce_y()

    if (ball.ball.xcor() > 600):
        score.p1_point()
        ball.reset_position()
    
    if (ball.ball.xcor() < -600):
        score.p2_point()
        ball.reset_position()

    # Detect collision with p1 paddle
    if (ball.ball.distance(player_1.paddle) < 40 and ball.ball.xcor() > -570):
        ball.bounce_x()
        ball.move()
    
    # Detect collision with p2 paddle
    if (ball.ball.distance(player_2.paddle) < 40 and ball.ball.xcor() < 570):
        ball.bounce_x()
        ball.move()
    
    #listen for p1 and p2 movement
    screen.onkey(player_1.up, "w")
    screen.onkey(player_1.down, "s")
    screen.onkey(player_2.up, "Up")
    screen.onkey(player_2.down, "Down")




# only close when we click on the screen
screen.exitonclick()