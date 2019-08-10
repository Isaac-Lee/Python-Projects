import turtle
n = int(input())
t = turtle.Turtle()
for i in range(n):
    t.forward(100)
    t.left(360/n)