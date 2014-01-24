"""
fibonacci.py

Calculates the 100th fibonacci number

"""

def fib(left, right, count):
    print left
    temp = right
    right = left + right
    left = temp
    count+=1
    if count < 100:
        fib(left, right, count)
    
fib(0,1,0)
