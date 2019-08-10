'''
원, 다각형 그리기
'''
import turtle
c=turtle.Turtle()
c.circle(50)

a=0
while a<8:
    c.forward(100)
    c.right(45)
    a+=1