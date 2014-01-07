"""
Pig Latin

This program translates and to and from pig latin.

"""
from collections import deque

class PigLatin:
    def __init__(self):
        self.cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        self.vowels = ['a','e','i','o','u']

    def translateToPigLatin(self,word):
        print "Here"
        wordDeque = deque(word)
        while wordDeque[0] in self.cons:
            wordDeque.append(wordDeque.popleft())
            
        wordDeque.append("ay")

        s = ""
        for word in wordDeque:
            s += word 
        print s
    
    def translateFromPigLatin(self, word):
        pass
    def main(self):
        print "Please enter a '1' if you want to translate to Pig Latin"
        choice = raw_input("Please a '2' if you want to translate from Pig Latin:> ")
        word = raw_input("What word would you like translated:> ")

        if choice is "1": self.translateFromPigLatin(word)
        if choice is "2": self.translateToPigLatin(word)
pigLatin = PigLatin()
pigLatin.main()

"""
Deque
while list[0] is in self.cons:
    pop X letter if consenant
        add X to back of 

"""
