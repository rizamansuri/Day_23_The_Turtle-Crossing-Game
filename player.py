from turtle import Turtle

START_POSITION = (0, -270)
FINAL_Y = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def up(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(START_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINAL_Y:
            return True
        else:
            return False
