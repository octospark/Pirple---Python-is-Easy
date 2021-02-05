''' The suggestion from the assignment was to import the module termcolor
but it did not work at all in my system. The other suggestion to use color
coded unicode characters was cool for a blue character but I couldn't find
a disk of another color. So just X-es and O-s.
'''

fieldMatrix = [[" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "]]

def drawField(fieldMatrix):
    for row in range(len(fieldMatrix)):
        print("|", end="")
        for column in range(len(fieldMatrix[0])):
            print(fieldMatrix[row][column] + "|", end="")
        print()
    print("---------------")


def setDisk(fieldMatrix, position, sign):
    ''' Set a disk in a given position in the matrix.
    If the operation is sucessful return true, otherwise return false.
    '''
    for row in range(len(fieldMatrix) - 1, -1, -1):
        if fieldMatrix[row][position] == " ":
            fieldMatrix[row][position] = sign
            return True
    return False

def isWinner(fieldMatrix, sign):
    # Check rows
    for i in range(len(fieldMatrix)):
        for j in range(0, len(fieldMatrix[i]) - 4):
            if fourOfTheSame(fieldMatrix[i][j:j+4], sign):
                return True
            

    # Check columns
    for k in range(len(fieldMatrix[0])):
        for m in range(len(fieldMatrix) - 3):
            partialColumn = []
            for n in range(4):
                partialColumn.append(fieldMatrix[m + n][k])
            if fourOfTheSame(partialColumn, sign):
                return True

    # Check left-up right-down diagonal
    for k in range(len(fieldMatrix[0]) - 4):
        for m in range(len(fieldMatrix) - 3):
            partialColumn = []
            for n in range(4):
                partialColumn.append(fieldMatrix[m + n][k + n])
            #print(partialColumn)
            if fourOfTheSame(partialColumn, sign):
                return True


    # Check left-down right-up
    for k in range(len(fieldMatrix[0]) - 3):
        for m in range(3, len(fieldMatrix)):
            partialColumn = []
            for n in range(4):
                partialColumn.append(fieldMatrix[m - n][k + n])
            if fourOfTheSame(partialColumn, sign):
                return True
        
    return False
        

def fourOfTheSame(partialList, sign):
    ''' Function that determines if four elements of a list are the same
    with the given argument (sign)'''
    for element in partialList:
        if element != sign:
            return False
    return True

def connectFour():
    ''' Player 1 has 'X' and player 2 has 'O'
    '''
    while True:
        token = 'X'
        position = int(input("Player 1 enter a row number: "))
        while not setDisk(fieldMatrix, position, token):
            position = int(input("Row is full. Player 1 enter a new row number: "))
        drawField(fieldMatrix)
        

        if isWinner(fieldMatrix, token):
            print('Player', token, "won!")
            break

        token = 'O'
        position = int(input("Player 2 enter a row number: "))
        while not setDisk(fieldMatrix, position, token):
            position = int(input("Row is full. Player 2 enter a new row number: "))
        drawField(fieldMatrix)
        

        if isWinner(fieldMatrix, token):
            print('Player', token, "won!")
            break

connectFour()
        

