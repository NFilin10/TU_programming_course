from turtle import *

def poora(n):
    return 360/n

def main(n, kraadid):
    if n == 0:
        return
    forward(100)
    left(kraadid)
    main(n-1, kraadid)
    
n = 5
main(n, poora(n))