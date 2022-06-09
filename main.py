from turtle import Screen
from paddle import Paddle
from net import Net
from ball import Ball
from score_board import Score
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=900, height=500)
screen.bgcolor("black")
screen.tracer(0)

my_paddle = Paddle(x_coordinate=-435, y_coordinate=0)
counter_paddle = Paddle(x_coordinate=425, y_coordinate=0)
game_net = Net()
the_ball = Ball()
player_score = Score()

screen.listen()
screen.onkey(fun=my_paddle.paddle_up, key="w")
screen.onkey(fun=my_paddle.paddle_down, key="s")
screen.onkey(fun=counter_paddle.paddle_up, key="Up")
screen.onkey(fun=counter_paddle.paddle_down, key="Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(the_ball.ball_speed)

    the_ball.move_ball()

    if the_ball.ycor() > 240 or the_ball.ycor() < -240:
        the_ball.bounce_ball_to_y()

    if the_ball.distance(my_paddle) < 30 and the_ball.xcor() > -425 or \
            the_ball.distance(counter_paddle) < 30 and the_ball.xcor() > 400:
        the_ball.bounce_ball_to_x()
        the_ball.move_ball()

    if the_ball.xcor() > 450:
        the_ball.move_ball()
        the_ball.reset_position()
        player_score.player1_score_increase()

    if the_ball.xcor() < -450:
        the_ball.move_ball()
        the_ball.reset_position()
        player_score.player2_score_increase()

screen.exitonclick()
