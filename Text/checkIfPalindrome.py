"""
checkIfPalindrome

Check if user inputted word is a palindrome
"""

def checkIfPalindrome(word):
    #add word or phrase to array
    palindrome = list(word)
    
    #iterate over word
    left = 0
    right = len(palindrome) - 1
    while left < right:
        if palindrome[left] is palindrome[right]:
            left += 1
            right -= 1
        else:
            return str(word) + " is NOT a palindrome"

    return str(word) + " is a palindrome"        


def __main__():
    while True:
        word = raw_input("Please enter a word that you want to check if it is a palidnrome:> ")    
        print checkIfPalindrome(str(word))

__main__()
