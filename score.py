from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=("Courier", 80, "normal"))
    
    def p1_point(self):
        self.p1_score += 1
        self.update_score()
    
    def p2_point(self):
        self.p2_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("#394f49")
        self.write("GAME OVER", align="center", font=("Courier", 80, "normal"))
        winner = 0
        if (self.p1_score > self.p2_score):
            winner = 1
        else:
            winner = 2
        self.goto(0, -100)
        self.color("#394f49")
        self.write(f" Player {winner} wins!", align="center", font=("Courier", 40, "normal"))