from turtle import Turtle
import random

COLOURS = ['orange', 'blue', 'pink', 'black', 'gold',
           'red', 'purple', 'green', 'brown']


class Car:
    """A class to represent a car for the Turtle Crossing game."""

    def __init__(self):
        self.all_cars = []
        self.car_speed = 20

    def new_car(self):
        """Makes a new car."""
        random_num = random.randint(1, 3)
        if random_num == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            random_y = random.randint(-240, 270)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def move(self):
        """Moves the car."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_car_speed(self):
        """Increase the speed of all the cars."""
        self.car_speed += 5
