"""
Counts the number of vowels in the
user inputted string
"""

my_set = ['a', 'e', 'i', 'o', 'u']

def vowel_counter(string):
    number_vowels = 0
    for a in string:
        if a in my_set:
            number_vowels += 1
    return number_vowels
    
def main():
    print "VOWEL COUNTER \n\n"
    print "Please enter a string to enter"

    number_of_vowels = raw_input("<:")
    print vowel_counter(number_of_vowels)

main()

