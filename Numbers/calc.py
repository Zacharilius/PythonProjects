"""
Calculator
This is a simple calculator that allows basic arithmetic
The user inputs 2 numbers and an operator.
A simple calculator to do basic operators.
"""

def main():
    number1 = input("Please input number 1: ")
    number2 = input("Please input number 2: ")
    operator = raw_input("Please input the operator '+,-,*, or /': ")

    if operator not in '+-*/':
        return "Enter a valid operator"
    elif operator is '+':
        calc =  number1 + number2
    elif operator is '-':
        calc = number1 - number2
    elif operator is '*':
        calc = number1 * number2
    elif operator is '/':
        calc = number1 / number2
    return str(number1) + " " + operator + " " + str(number2) + " = " + str(calc)

print main()
