from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(40)
        self.shape("circle")
        self.shapesize(stretch_wid=0.9, stretch_len=0.9)
        self.color("yellow")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ball_to_y(self):
        self.y_move *= -1

    def bounce_ball_to_x(self):
        self.ball_speed *= 0.9
        self.x_move *= -1

    def clear_the_ball(self):
        self.clear()

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_ball_to_x()
