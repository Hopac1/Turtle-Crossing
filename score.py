from turtle import Turtle


class Score(Turtle):
    """A class that represents a scoreboard."""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.lives = 3
        self.hideturtle()
        self.penup()

    def show_level(self):
        """Displays the current level on screen."""
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align='left', font=('Arial', 25,
                                                               "normal"))
        self.goto(280, 260)
        self.write(f"Lives: {self.lives}", align='right', font=('Arial', 25,
                                                               "normal"))

        self.clear()

    def next_level(self):
        """Increases level count by 1."""
        self.level += 1

    def lose_life(self):
        """Reduces the amount of lives by 1."""
        self.goto(0, 0)
        self.write(f"Squish!", align='center', font=('Arial', 25,
                                                               "normal"))

        self.lives -= 1

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write(f"GAME OVER", align='center', font=('Arial', 25,
                                                               "normal"))
