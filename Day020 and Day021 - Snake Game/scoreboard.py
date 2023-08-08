from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier",18,"normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        #open the data file to read and set the highscore
        with open("data.txt") as file:
            high_score = file.read()
        self.score = 0
        self.high_score = int(high_score )
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score= self.score
            #open the data file and update the new hight score
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


"""
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!",align=ALIGMENT, font=FONT)
        """