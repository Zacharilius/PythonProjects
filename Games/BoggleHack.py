#Boggle hack
#Word Matrix
class BoggleWordFinder:
    def __init__(self):
        self.data = []
        
    def createMatrix(self):
        letterMatrix = [
                    ['m', 'a', 'p'],
                    ['i', 's', 'l'],
                    ['t', 'q', 'e']]
        print len(letterMatrix)
        print len(letterMatrix[0])
        return letterMatrix
    def formatPrintMatrix(self, matrix):
        x = 0
        while x < len(matrix):
            j = 0
            line = ""
            while j < len(matrix[x]):
                line += str(matrix[x][j])
                j += 1
            x += 1
            print line + "\n"
    #Add all good words to hash set


    #


    def findWords(self):
        pass



bwf = BoggleWordFinder()
matrix = bwf.createMatrix
bwf.formatPrintMatrix(matrix)
print "yep"
