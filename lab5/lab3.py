'''
원의 반지름 r, 좌표 (0,0) 기준으로 원을 그린 후 -r~r범위를 갖는 난수 x,y를 생성해서
x,y가 원 안에 들어가 있으면 빨간점, 밖이면 그냥 기본점을 찍어 100번 반복하는 프로그램을 작성하시오
'''
import turtle
import random
t = turtle.Turtle()
r = int(input("원의 반지름을 입력하세요: "))
t.ht()
t.up()
t.goto(0,-r)
t.down()
t.circle(r)
for i in range(100):
    t.up()
    x = random.randint(-r, r)
    y = random.randint(-r, r)
    t.goto(x, y)
    t.down()
    if (x*x + y*y) <= r*r:
        t.dot('red')
    else:
        t.dot()
