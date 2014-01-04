"""
Fibonnacci Generator

Calculates  numbers in the fibonacci sequence that are less that 1000.
"""

def fibonnacciGenerator():
    x,y = 0,1
    while x < 1000:
        yield str(x) + " "
        x,y = y, x+y

for i in fibonnacciGenerator():
    print i
