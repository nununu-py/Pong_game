from turtle import Turtle


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setheading(90)
        self.penup()
        self.color("white")
        self.y_coordinate = -240
        self.goto(0, self.y_coordinate)
        self.make_net()

    def make_net(self):
        while self.y_coordinate < 240:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            self.y_coordinate += 20
