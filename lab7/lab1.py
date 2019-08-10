"""
박스를 그리고 박스 안에서거북이가 세모들을 피하는 게임을 작성한다.
프로그램 순서
- 박스를 그린다.
- 거북이를 생성한다.
- 일정 시간마다 세모를 생성한다.
- play함수를 일정 시간마다 실행한다.

일정 시간마다 생성한 세모는 list형식으로 세모와 방향을 저장해서 play함수에 이용
play함수는 playing이 True일때 생성된 세모들을 이동, 세모가 박스에 부딛히면 반대방향으로 이동
입력하는 방향으로 거북이를 이동, 세모와  부딛히면 playing을 Flase로 설정
"""

import random
import turtle

t = turtle.Turtle()  # 사용자 터틀
tris = []  # 만들어진 삼각형 보관하는 리스트

# 방향키 상태 초기갓
right_key = False
left_key = False
up_key = False
down_key = False

# 박스 그리기 함수
def draw_sq():
    t.penup()
    t.goto(-100,100)
    t.pendown()
    t.pencolor('green')
    for i in range(4):
        t.forward(200)
        t.right(90)

# 거북이 생성
t.goto(0,0)
t.shape("turtle")

# 방향이동
# -대각선이동
'''
각 키별로 눌리면 Ture, 떨어지면 False로 바뀐다.
그래서 두가지가 같이 눌리면 거북이가 보는 heading의 각도가 바뀌는 식으로 구현
키를 입력한하면 앞으로 가는중으로 구현
'''
def trun_right():
    global right_key = True
    t.setheading(0)

def trun_left():
    global left_key = True
    t.setheading(180)

def trun_up():
    global up_key = True
    t.setheading(90)

def trun_down():
    global down_key = True
    t.setheading(270)

def off_trun_right():
    global right_key = False

def off_trun_left():
    global left_key = False

def off_trun_up():
    global up_key = False

def off_trun_down():
    global down_key = False

# 삼각형 객체 생성:
class Tri:
    tri = turtle.Turtle()  # 삼각형 만드는 터틀

    def Tri():  # 삼각형 만드는 함수
        tri.penup()
        tri.goto(random.randint(-100,100), random.randint(-100,100))  # 랜덤한 위치로 이동
        tri.right(random.randint(0, 360))  # 랜덤한 해딩
        tri.pendown()  # 본격 삼각형 그리기
        tri.fillcolor('red')
        for n in range(3):
            tri.forward(10)
            tri.right(120)

    # 삼각형 위치 반환 함수
    def triPosition():
        tri.position()

    # 삼각형이 튕기는 거

# 만났는지 체크
def is_touch():

# 거북이들이 입력대로 움직이는 코드
# 삼각형들이 벽에 부딛히면 튕기게 하는 코드
# 위함수를 이용해


# 사각형을 만드는 함수, 매순간 객체를 생성해야함.
def makeTri():
# play함수
'''
부딛히는 거는 거북이의 좌표와 삼각형의 좌표값이 일정 수준으로 가까워지면 부딛히는 것
'''
# 방향키 상태 초기갓
right_key = False
left_key = False
up_key = False
down_key = False
"""
onkeypress 함수는 누르고 있을때만 작동함
"""
def play():
    while (playing == True):  # True인 중에서만 게임 작동

