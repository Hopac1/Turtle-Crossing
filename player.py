from turtle import Turtle

START_POS = -280


class Player(Turtle):
    """A class to represent the Player's character."""

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('cyan')
        self.penup()
        self.player_speed = 20
        self.speed("fastest")
        self.left(90)
        self.sety(START_POS)

    def move(self):
        """Moves the turtle upwards."""
        new_y = self.ycor()
        new_y += 20
        self.goto(0, new_y)

    def reset_position(self):
        """Resets the player's position back to the start."""
        self.sety(START_POS)