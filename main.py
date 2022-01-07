from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Dectect collision with food
    if snake.segments[0].distance(food) < 15:
        scoreboard.increaseScore()
        food.refresh()
        snake.extend_snake()
    #Detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_on = False
        scoreboard.game_over()


    #Dectec collision with tail
    for segment in snake.segments[1: ]:
        if snake.segments[0].distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
screen.exitonclick()
