import turtle
import random


# 사각형을 그리는 함수
def draw_sq(t, distance=400):
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    t.pencolor('green')
    for i in range(4):
        t.forward(distance)
        t.right(90)
    t.penup()
    t.goto(0, 0)


# 삼각형 터틀을 만들고 랜덤한 위치,랜덤한 방향으로 설정해 l_tri의 리스트에 저장하는 함수
def add_tri():
    tri = turtle.Turtle()  # 삼각형 만드는 터틀
    tri.penup()
    tri.goto(random.randint(-200, 200), random.randint(-200, 200))
    tri.shape("triangle")
    tri.setheading(random.randint(0, 360))
    tri.speed(0)
    l_tri.append(tri)


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


def is_touch(player, triangle, threshold=10):
    global playing
    tur_xcor = player.xcor()
    tur_ycor = player.ycor()

    # 삼각형들과 거북이가 부딛혔는지 판단해 부딛히면 playing을 False로 바꾸는 함수
    if triangle.distance(tur_xcor, tur_ycor) <= threshold:
        playing = False
    else:
        playing = True
    # triangle은 삼각형, threshold는 판단하는 기준거리, x,y는 거북이의 위치


# 벽에 부딪혔는지 체크후 heading을 바꾸는 함수
def touch_wall_check(tri):
    tri_xcor = tri.xcor()
    tri_ycor = tri.ycor()

    if tri_xcor >= 200:
        if tri.heading() < 90:
            tri.setheading(tri.heading() + (90 - tri.heading()) * 2)
        elif tri.heading() > 270:
            tri.setheading(tri.heading() + (270 - tri.heading()) * 2)
        else:
            tri.setheading(180)

    elif tri_ycor >= 200:
        if tri.heading() > 90:
            tri.setheading(tri.heading() + (180 - tri.heading()) * 2)
        elif tri.heading() < 90:
            tri.setheading(tri.heading() - tri.heading() * 2)
        else:
            tri.setheading(270)

    elif tri_xcor <= -200:
        if tri.heading() > 180:
            tri.setheading(tri.heading() + (270 - tri.heading()) * 2)
        elif tri.heading() < 180:
            tri.setheading(tri.heading() - (tri.heading() - 90) * 2)
        else:
            tri.setheading(0)

    elif tri_ycor <= -200:
        if tri.heading() < 270:
            tri.setheading(tri.heading() - (tri.heading() - 180) * 2)
        elif tri.heading() > 270:
            tri.setheading(tri.heading() + (360 - tri.heading()) * 2)
        else:
            tri.setheading(90)


def timer_go():
    # heading은 거북이의 방향
    # 거북이들을 입력대로 움직이는코드
    global heading
    global up
    global left
    global down
    global right
    global playing
    global t
    if playing:

        if up:
            if right:
                heading = 45
            elif left:
                heading = 135
            elif down:
                heading = heading
            else:
                heading = 90
        if down:
            if right:
                heading = 315
            elif left:
                heading = 225
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
        t.forward(5)

    t.setheading(heading)
    t.forward(5)
    # 삼각형들이 벽에 부딛히면 튕기게 방향을 바꾸는 코드
    for tri in l_tri:
        touch_wall_check(tri)
        # 위 함수를 이용해 삼각형들이 거북이와 부딛혔는지 확인
        is_touch(t, tri)
        # 삼각형들을 움직이는 코드
        tri.forward(5)
    # playing이 아닐때 FAIL을 출력하는 코드


up = False
down = False
right = False
left = False
playing = True
heading = 0
l_tri = []

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
draw_sq(t)
screen = t.screen



# 삼각형을 미리 3개 추가한후 실행
for i in range(3):
    add_tri()

time = 0
while playing:
    time += 1
    screen.listen()
    timer_go()
    if time == 250:
        t.write("성공!\n\n")  # 끝나고 성공했으면 success를 쓰는 함수
        break

# 끝나고 성공했으면 success를 쓰는 함수
# def printSucces():

screen.listen()
screen.mainloop()
