import turtle


def go_left():
    t.left(10)
    t.forward(10)


def go_right():
    t.right(10)
    t.forward(10)


def draw_maze(x, y):
    for i in range(2):
        t.penup()
        if i == 1:
            t.goto(x + 100, y + 100)
        else:
            t.goto(x, y)
        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)


t = turtle.Turtle()
s = turtle.Screen()
s.onkey(go_left, "Left")
s.onkey(go_right, "Right")

t.shape("turtle")
t.speed(100)
draw_maze(-300, 200)

t.penup()
t.goto(-300, 250)
t.pendown()
s.listen()
s.mainloop()
