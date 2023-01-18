
from turtle import *

def abi(suund, n, pikkus):
    if n < 0:
        return
    for i in range(3):
        forward(pikkus)
        abi(suund, n-1, pikkus/2)
        if n == 0:
            if suund == "parem":
                right(90)
            else:
                left(90)
    forward(pikkus)
    
def fraktal(n, pikkus):
    if n % 2 == 0:
        suund = "vasak"
    else:
        suund = "parem"
    abi(suund, n-1, 100)
    
fraktal(2, 100)