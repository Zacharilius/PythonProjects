"""
binary to decimal number converter
The program asks the user if they want to convert from binary
to decimal or from decimal to binary. The program then prompts
the user to enter a number. It then prints out the converted
number.

"""
class Conversion:
    #decimal to binary function
    def decimalToBinaryConversion(self, decimal):
        if decimal < 0:
            return "ERROR:The number must be positive"
        elif decimal == 0:
            return "0"
        else:
            return self.decimalToBinaryConversion(decimal//2) + str(decimal%2)

    #binary to decimal function
    def binaryToDecimalConversion(self, binary):
        if binary < 0:
            return "Error: The number must be positive"
        decimal = 0
        for i in range(len(str(binary))):
            power = len(str(binary))-(i+1)
            decimal += int(str(binary)[i]) * (2**power)
        return decimal

    #main method
    def main(self):
        print "Welcome to the converter"
        print "Press 1 to convert from decimal to binary"
        print "Press 2 to convert from binary to decimal"

        choice = input(">")
        print "You chose: " + str(choice)

        print "What number would you like to convert"
        numberToConvert = input(">")
        
        if(choice is 1):
            print self.decimalToBinaryConversion(numberToConvert)
        elif(choice is 2):
            print self.binaryToDecimalConversion(numberToConvert)
        else:
            print "ERROR: Unrecognized choice"
    def __init__(self):
        self.data = []
    
conv = Conversion()
conv.main()
