from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(x_coordinate, y_coordinate)
        self.shapesize(stretch_wid=4, stretch_len=1)

    def paddle_up(self):
        new_y_cor = self.ycor()
        new_y_cor += 35
        new_x_cor = self.xcor()
        self.goto(new_x_cor, new_y_cor)

    def paddle_down(self):
        new_y_cor = self.ycor()
        new_y_cor -= 35
        new_x_cor = self.xcor()
        self.goto(new_x_cor, new_y_cor)
