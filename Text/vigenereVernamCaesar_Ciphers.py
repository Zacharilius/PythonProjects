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
        return vigenereTable
            
    def createPassPhrase(self,wordToEncodeOrDecode, passPhrase):
        #creates a passphrase the same length as the word to encode, if necessary
        count = 0
        while len(wordToEncodeOrDecode) > len(passPhrase):
            if count >= len(passPhrase):
                count = 0
            passPhrase += passPhrase[count]
            count += 1

        #creates an array of characters in integer representation of the wordToEncode and the passPhrase
        #Stops encoding if not all letter and returns "Unrecognized input"
        encodedWord = ""
        charEncNum=[]
        charPassNum=[]
        for letter in wordToEncodeOrDecode:
            encNum = ord(letter)
            if encNum < 91 and encNum >= 65:
                charEncNum.append(encNum)
            else:
                return "Unreconized input"
        for letter in passPhrase:
            passNum = ord(letter)
            if passNum < 91 and passNum >= 65:
                charPassNum.append(passNum)
            else:
                return "Unrecognized input"
        return (charEncNum, charPassNum)

    def encode(self, wordToEncode,passPhrase, vigenereTable):
        #strips spaces and turns into uppercase
        wordToEncode = wordToEncode.strip().upper()
        passPhrase = passPhrase.strip().upper()
        #prints word to encode and the pass phrase
        print "Word to encode: " + wordToEncode
        print "Pass phrase: " + passPhrase

        createPassPhraseOutput = self.createPassPhrase(wordToEncode, passPhrase)
        charEncNum, charPassNum = createPassPhraseOutput

        #Reference the 2d array aka the vigenere table to encode the word or phrase
        count = 0
        encodedOutput = ""
        while count < len(charEncNum):
            encodedOutput += vigenereTable[charEncNum[count]-65][charPassNum[count]-65]
            count += 1
        return encodedOutput
        
        
    def decode(self, wordToDecode, passPhrase, vigenereTable):
        print "Word to decode: " + wordToDecode
        print "Pass phrase: " + wordToEncode
        createPassPhraseOutput = self.createPassPhrase(wordToEncode, passPhrase)
        
        count = 0
        encodedOutput = ""
        while count < len(charEncNum):
            encodedOutput += vigenereTable[charEncNum[count]-65][charPassNum[count]-65]
            count += 1
        return encodedOutput
                        
    def __init__(self):
        self.data = []
        
    def main(self):
        vigenereTable = vig.createVigenereTable()
        encodedWord = vig.encode("nope ", "yep ", vigenereTable)
        print "Encoded word: " + encodedWord
        print "Decoded word: " + vig.encode(encodedWord, "yep ", vigenereTable)


vig = VigenereCipher()
vig.main()
