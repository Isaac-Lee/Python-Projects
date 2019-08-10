from turtle import *
import turtle


class Ball:
    def __init__(self, color, size, speed):
        self.x = 0
        self.y = 0
        self.xSpeed = speed
        self.ySpeed = speed
        self.turtle = Turtle()
        self.turtle.shape("circle")
        self.turtle.shapesize(size)
        self.turtle.color(color)

    def move(self):
        self.x += self.xSpeed
        self.y += self.ySpeed
        self.turtle.goto(self.x, self.y)

s = turtle.Screen()

ball = Ball("red", 2, 1)

for i in range(100):
    ball.move()

s.mainloop()



