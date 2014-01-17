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
            
    def createPassPhrase(self, wordToEncodeOrDecode, passPhrase):
        #creates a passphrase the same length as the word to encode, if necessary
        count = 0
        while len(wordToEncodeOrDecode) > len(passPhrase):
            if count >= len(passPhrase):
                count = 0
            passPhrase += passPhrase[count]
            count += 1
        return passPhrase
    
    def createPassPhraseNum(self,wordToEncodeOrDecode, passPhrase):
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
                return "Unreconized input 1"
        for letter in passPhrase:
            passNum = ord(letter)
            if passNum < 91 and passNum >= 65:
                charPassNum.append(passNum)
            else:
                return "Unrecognized input 2"
        return (charEncNum, charPassNum)

    def encode(self, wordToEncode,passPhrase, vigenereTable):
        #strips spaces and turns into uppercase
        wordToEncode = wordToEncode.strip().upper()
        passPhrase = passPhrase.strip().upper()
        #prints word to encode and the pass phrase
        print "Word to encode: " + wordToEncode
        print "Pass phrase: " + passPhrase

        createPassPhraseOutput = self.createPassPhraseNum(wordToEncode, self.createPassPhrase(wordToEncode, passPhrase))
        charEncNum, charPassNum = createPassPhraseOutput

        #Reference the 2d array aka the vigenere table to encode the word or phrase
        count = 0
        encodedOutput = ""
        while count < len(charEncNum):
            encodedOutput += vigenereTable[charEncNum[count]-65][charPassNum[count]-65]
            count += 1
        return encodedOutput
        
        
    def decode(self, wordToDecode, passPhrase, vigenereTable):
        #strips spaces and turns into uppercase
        wordToDecode = wordToDecode.strip().upper()
        passPhrase = passPhrase.strip().upper()
        print "Word to decode: " + wordToDecode
        print "Pass phrase: " + passPhrase

        createPassPhraseOutput = self.createPassPhraseNum(wordToDecode, self.createPassPhrase(wordToDecode, passPhrase))
        charEncNum, charPassNum = createPassPhraseOutput
        
        count = 0
        decodedOutput = ""
        while count < len(charEncNum):
            #find correct column based on pass phrase letter
            column = vigenereTable[charPassNum[count]-65]

            decodedOutput += vigenereTable[0][column.index(wordToDecode[count])]
            #encodedOutput += vigenereTable[charEncNum[count]-65][self.createPassPhrase().index(passPhrase[count])] #PROBLEM
            count += 1
        return decodedOutput
        #then search using .index() to to find letter from encoded word in column
        #then add column 0 and row of .index() to translated word
    def __init__(self):
        self.data = []
        
    def main(self):
        vigenereTable = vig.createVigenereTable()
        encodedWord = vig.encode("alphabet ", "yep ", vigenereTable)
        print "Encoded word: " + encodedWord
        print "Decoded word: " + vig.decode(encodedWord, "yep ", vigenereTable)


vig = VigenereCipher()
vig.main()
