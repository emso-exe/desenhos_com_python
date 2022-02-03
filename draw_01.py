# -*- coding: utf-8 -*-

import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()

s.colormode(255)
s.bgcolor(0, 0, 0)

t.speed(0)
t.width(1)
# t.pencolor(0,255,0)

seq = []
for i in range(0, 256):
    seq.append(i)

qes = []
qes = seq[::-1]

seq.extend(qes)


def shape(angle, side, limit, n, seq):

    n += 1
    t.pencolor(0, 0, seq[n])

    print(n)

    reverseDirection = 200
    t.forward(side)

    if side % (reverseDirection*2) == 0:
        angle = angle + 2
        print(side)
    elif side % reverseDirection == 0:
        angle = angle - 2
        print(side)

    t.right(angle)
    side = side + 2
    if side < limit:
        shape(angle, side, limit, n, seq)


n = 0
angle = 119
side = 0
limit = 1020
shape(angle, side, limit, n, seq)

turtle.done()
