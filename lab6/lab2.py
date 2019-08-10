# 프렉탈 나무 만들기
import turtle


def tree(length):
    if length > 5:
        t.forward(length)
        t.right(20)
        tree(length - 10)
        t.left(40)
        tree(length - 10)
        t.right(20)
        t.backward(length)


t = turtle.Turtle()
t.penup()
t.goto(0, -300)
t.pendown()
t.speed(100)
t.left(90)
t.pencolor("green")
tree(85)
turtle.done()