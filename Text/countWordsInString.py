"""
countWordsInString

Prompts the user and prints the number of words in the user i nputted string

"""

def getNumberWords(word):
    return len(word)

def main():
    while True:
        word = raw_input("What word do you want to know the number of letters in:> ")
        print getNumberWords(word)
main()
