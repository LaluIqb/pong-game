from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.score()

    def score(self):
        self.clear()
        self.goto((-80, 230))
        self.write(self.left_score, align='center', font=('Courier', 40, 'normal'))
        self.goto((80, 230))
        self.write(self.right_score, align='center', font=('Courier', 40, 'normal'))

    def goal_right(self):
        self.left_score += 1
        self.score()

    def goal_left(self):
        self.right_score += 1
        self.score()
