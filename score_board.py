from turtle import Turtle
TEXT = ("Arial", 12, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 225)
        self.color("pink")
        self.left_score = 0
        self.right_score = 0
        # self.speed("fastest")
        self.write(arg=f"Player1 Score : {self.left_score}    Player2 Score : {self.right_score}",
                   align="center", font=TEXT)

    def player1_score_increase(self):
        self.left_score += 1
        self.clear()
        self.write(arg=f"Player1 Score : {self.left_score}    Player2 Score : {self.right_score}",
                   align="center", font=TEXT)

    def player2_score_increase(self):
        self.right_score += 1
        self.clear()
        self.write(arg=f"Player1 Score : {self.left_score}    Player2 Score : {self.right_score}",
                   align="center", font=TEXT)
