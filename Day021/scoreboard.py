from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def r_player_scores(self):
        self.r_score += 1
        #print("Right Player Scores:",self.r_score)
        self.update_score_board()

    def l_player_scores(self):
        self.l_score += 1
        #print("Left Player Scores:", self.l_score)
        self.update_score_board()
