"""
vigenereVernamCaesar_Ciphers

Uses a vigenere cipher to encode and decode plain text
"""

class VigenereCipher:
    def createVigenereTable(self):
        vigenereTable = []
        for arr in xrange(26):
            vigenereTable.append([])
        x = 0
        for arr in vigenereTable:
            offset = 26
            for row in xrange(26):
                if 65 + row >= 65 + offset:
                    letter = str(chr(65 + row - 25))
                else:
                    letter = str(chr(65 + row))
                vigenereTable[x].append(letter)
            x += 1
        print vigenereTable
        
    def __init__(self):
        self.data = []


vig = VigenereCipher()
vig.createVigenereTable()
