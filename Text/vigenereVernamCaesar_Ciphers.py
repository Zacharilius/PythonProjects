"""
vigenereVernamCaesar_Ciphers

Uses a vigenere cipher to encode and decode plain text
"""

class VigenereCipher:
    #Creates a vigener table
    def createVigenereTable(self):
        vigenereTable = []
        for arr in xrange(26):
            vigenereTable.append([])
        x = 0
        letterStart = 65
        for arr in vigenereTable:
            string = ""
            for row in xrange(26):
                if letterStart + row > 90:
                    letter = str(chr(letterStart + row - 26))
                else:
                    letter = str(chr(letterStart + row))
                vigenereTable[x].append(letter)
                string += " " + letter
            letterStart += 1
            x += 1
            print string
    def createPassPhrase(self,word):
        pass

    def encode(self, wordToEncode,passPhrase):
        if len(wordToEncode) < len(passPhrase):
            print "Yep"
        
    def decode(self, wordToDecode, passPhrase):
        pass
                
    def __init__(self):
        self.data = []


vig = VigenereCipher()
vig.createVigenereTable()
vig.encode("yep", "nope")
