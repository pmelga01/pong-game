from turtle import Turtle

class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.x_move = 25
        self.ball.y_move = 25
        self.ball.speed("fastest")

    def move(self):
        new_x = self.ball.xcor() + self.ball.x_move
        new_y = self.ball.ycor() + self.ball.y_move
        self.ball.goto(new_x, new_y)

    def bounce_y(self):
        self.ball.y_move *= -1

    def bounce_x(self):
        self.ball.x_move *= -1

    def reset_position(self):
        self.ball.goto(0,0)
        self.bounce_x()
