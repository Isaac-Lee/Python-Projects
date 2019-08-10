import turtle

def tree(d):
    if d<10:
        pass
    else:
        t.fd(d)
        t.rt(30)
        tree(d-15)
        t.lt(60)
        tree(d-15)
        t.rt(30)
        t.backward(d)

t = turtle.Turtle()
t.left(90)
tree(100)