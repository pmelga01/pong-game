from turtle import Turtle

class Paddle:
    def __init__(self, position):
        self.paddle = Turtle()
        self.paddle.speed("fastest")
        self.paddle.shape("square")
        self.paddle.color("#330f0a")
        self.paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle.penup()
        self.paddle.goto(position)
    
    def up(self):
        if (self.paddle.ycor() > 230):
            return
        new_y = self.paddle.ycor() + 25
        self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        if (self.paddle.ycor() < -230):
            return
        new_y = self.paddle.ycor() - 25
        self.paddle.goto(self.paddle.xcor(), new_y)