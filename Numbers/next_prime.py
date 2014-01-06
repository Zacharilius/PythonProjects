"""
Next prime

Finds the next prime number after the user inputted number

"""

class PrimeNumber:
    #Returns true even && false if odd
    def evenOrOdd(self, num):
        if num % 2 is 0:
            return True
        else:
            return False

    def isPrime(self, num):
        if num <= 0:
            return "is negative"
        #check if it is 1
        elif num is 1:
            return "is not prime"
        #check if it is 2
        elif num is 2 or num is 3:
            return "is prime"
        #
        elif self.evenOrOdd(num):
            return "is even and is NOT prime"
        else:
            x = 3
            while x < num:
                if num % x is 0:
                    return "is odd and is NOT prime"
                else:
                    x += 2
            return "is prime"
    def __init__(self):
        self.data = []
        

def test():
    prime = PrimeNumber()
    x = 0
    
    while x < 100:
        print "The number " + str(x) + " " + str(prime.isPrime(x))
        x += 1

test()
