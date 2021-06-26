from turtle import Screen
from player import Player
from score import Score
from car import Car
import time

# Screen setup
screen = Screen()
screen.setup(height=600, width=600)
screen.title("Turtle Crossing")
screen.bgcolor('grey')
screen.tracer(0)

player = Player()
car = Car()
score = Score()

# Keyboard controls
screen.listen()
screen.onkey(fun=player.move, key='w')

game_on = True
# Main loop
while game_on:
    time.sleep(0.1)
    screen.update()
    score.show_level()
    car.new_car()
    car.move()

    # Detect player collision with cars
    for sep_car in car.all_cars:
        if player.distance(sep_car) < 15:
            score.lose_life()
            time.sleep(1)
            player.reset_position()

    # Detect player successfully reaching top of the screen
    if player.ycor() >= 270:
        score.next_level()
        car.increase_car_speed()
        player.reset_position()
        time.sleep(0.5)

    if score.lives == 0:
        screen.clear()
        screen.bgcolor('grey')
        score.game_over()
        time.sleep(5)
        game_on = False

    # screen.exitonclick()
