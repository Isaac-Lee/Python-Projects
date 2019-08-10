import turtle

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


def turn_right():
    global right
    right = True

def turn_left():
    global left
    left = True

def turn_up():
    global up
    up = True

def turn_down():
    global down
    down = True

def _turn_right():
    global right
    right = False

def _turn_left():
    global left
    left = False

def _turn_up():
    global up
    up = False

def _turn_down():
    global down
    down = False

def timer_go():
    global heading
    global up
    global left
    global down
    global right
    if up:
        if right:
            heading=45
        elif left:
            heading=135
        elif down:
            heading = heading
        else:
            heading=90
    if down:
        if right:
            heading=315
        elif left:
            heading=225
        elif up:
            pass
        else:
            heading = 270
    if left:
        if right:
            heading = heading
        elif up:
            pass
        elif down:
            pass
        else:
            heading = 180
    if right:
        if left:
            pass
        elif up:
            pass
        elif down:
            pass
        else:
            heading = 0

    t.setheading(heading)
    t.forward(1)

up = False
down = False
right = False
left = False
heading = 0

t = turtle.Turtle()
screen = t.screen
t.speed(0)


draw_maze(-300, 200)
t.up()
t.goto(-300, 300)
t.down()

screen.onkeypress(turn_right, 'Right')
screen.onkeypress(turn_left, 'Left')
screen.onkeypress(turn_up, 'Up')
screen.onkeypress(turn_down, 'Down')
screen.onkeyrelease(_turn_right, 'Right')
screen.onkeyrelease(_turn_left, 'Left')
screen.onkeyrelease(_turn_up, 'Up')
screen.onkeyrelease(_turn_down, 'Down')

i = 1

while True:
    screen.ontimer(timer_go, i*30)
    i += 1
    if i>10000:
        break

screen.listen()
screen.mainloop()
