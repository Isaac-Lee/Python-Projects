import turtle


def frac(leng, d):
    if d == 0:

        t.fd(leng)

    else:

        leng = leng / 3

        d = d - 1

        frac(leng, d)

        t.lt(60)

        frac(leng, d)

        t.rt(120)

        frac(leng, d)

        t.lt(60)

        frac(leng, d)


t = turtle.Turtle()
t.speed(0)

for i in range(3):

    frac(200, 1)

    t.rt(120)

turtle.done()
