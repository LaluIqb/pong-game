import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

for width in range (-300, 301, 35):
    line = Turtle('square')
    line.color('white')
    line.penup()
    line.shapesize(stretch_len=0.1, stretch_wid=1)
    line.goto(0, width)


ball = Ball()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')
screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')

is_playing = True
while is_playing:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 or ball.distance(right_paddle) < 50 and ball.xcor() > 320 :
        ball.bounce_x()

    if ball.xcor() <= -400:
        ball.reset_position()
        scoreboard.goal_right()

    if ball.xcor() >= 400:
        ball.reset_position()
        scoreboard.goal_left()

screen.exitonclick()
