"""
factorial.py
Finds the greatest number

"""

class factorial:

    def __init__(self):
        pass
    def factor(self, number):
        if number is 0:
            return 1
        return number * self.factor(number - 1)


f = factorial()
print f.factor(4)
