"""
Pig Latin

This program translates and to and from pig latin.

"""
class PigLatin:
    def __init__(self):
        self.cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        self.vowels = ['a','e','i','o','u']

    def translateToPigLatin(self,word):
        pass
    def translateFromPigLatin(self, word):
        pass
    def main(self):
        print "Please enter a '1' if you want to translate to Pig Latin"
        choice = raw_input("Please a '2' if you want to translate to from Pig Latin:> ")
        word = raw_input("What word would you like translated:> ")

        print len(self.cons)
        print len(self.vowels)
        if choice is 1: translateFromPigLatin(word)
        if choice is 2: translateToPigLatin(word)
pigLatin = PigLatin()
pigLatin.main()
