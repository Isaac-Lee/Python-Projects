# 코흐 삼각별 만들기
import turtle
t = turtle.Turtle()
t.speed(0)
def frac(leng, d):
    if d ==0:
        t.forward(leng)
    else:
        leng = leng / 3
        d -= 1
        frac(leng, d)
        t.left(60)
        frac(leng, d)
        t.right(120)
        frac(leng, d)
        t.left(60)
        frac(leng, d)
for i in range(3):
    frac(300, 4)
    t.right(120)
