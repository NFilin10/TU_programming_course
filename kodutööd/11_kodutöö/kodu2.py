import turtle
from math import sqrt

def rec(h):
    if h < 1:
        return 1
    else:
        turtle.forward(h)
        turtle.left(180)
        turtle.forward(h/2)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(180)
        turtle.forward(h/2)
        turtle.left(90)
        return rec(h/sqrt(2))

rec(200)