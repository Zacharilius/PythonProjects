"""
Change
Calculates the number of bills and change to give back

"""

def calcChange(money):
    output = ""
    if money >= 100:
        output += str(money / 100) + " $100s, "
        money = money % 100
    if money >= 20:
        output += str(money / 20 ) + "$20s, "
        money = money % 20
    if money >= 10:
        output += str(money / 10) + "$10s, "
        money = money % 10
    if money >= 5:
        output += str(money / 5) + "$5s, "
        money = money % 5
    if money >= 1:
        output += str(money / 1) + "$1s, "
        money = money % 1
    if money >= .25:
        output += str(money / .25) + "quarters, "
        money = money % .25
    if money >= .10:
        output += str(money / .1) + "dimes, "
        money = money % .1
    if money >= .05:
        output += str(money / .05) + "nickels, & "
        money = money % .05
    if money >= .01:
        output += str(money / .01) + "pennies"
    return output
print calcChange(121)
