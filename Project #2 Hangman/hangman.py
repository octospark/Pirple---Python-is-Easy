'''This game works best if you execute the script from the terminal
and not from the IDLE console.
'''
import os, random
gameType = int(input("Do you want to play against Computer (0) or Player (1)? "))
if gameType == 0:
    fileList = [word.strip() for word in open('words.txt', 'r')]
    secretWord = random.choice(fileList)
else:
    secretWord = input("Player 1 enter your word: ")
    os.system('cls')


gallowGrid = [[' ', ' ', '|', '-', '-', '-', '|', ' '],
              [' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
              ['-', '-', '-', '-', '-', ' ', ' ', ' ']]

def drawGrid():
    for row in range(len(gallowGrid)):
        for column in range(len(gallowGrid[0])):
            print(gallowGrid[row][column], end='')
        print()

def gameStep(gallowGrid, mistakes):
    if mistakes == 1:
        gallowGrid[1][6] = 'O'
    elif mistakes == 2:
        gallowGrid[2][6] = '|'
    elif mistakes == 3:
        gallowGrid[1][5] = '\\'
    elif mistakes == 4:
        gallowGrid[1][7] = '/'
    elif mistakes == 5:
        gallowGrid[3][5] = '/'
    elif mistakes == 6:
        gallowGrid[3][7] = '\\'
    
def maskedWord(word):
    masked = ''
    for letter in word:
        if letter == ' ':
            masked += ' '
        else:
            masked += '-'
    return masked

def unmaskWord(guessLetter, maskedWord, secretWord):
    '''This function will update the masked word bsed on the guess of
    player 2.
    '''
    newMaskedWord = ''
    for i in range(len(secretWord)):
        if secretWord[i] == guessLetter:
            newMaskedWord += guessLetter
        else:
            newMaskedWord += maskedWord[i]
    return newMaskedWord

def rightLetter(guessLetter, secretWord):
    if guessLetter in secretWord:
        return True
    return False

masked = maskedWord(secretWord)

mistakes = 0
winner = False
drawGrid()

while mistakes != 6 and not winner:
    print("\"" + masked + "\"")
    guessLetter = input("Enter your guess: ")
    if not rightLetter(guessLetter, secretWord):
        mistakes += 1
    else:
        masked = unmaskWord(guessLetter, masked, secretWord)
    if masked == secretWord:
        winner = True
        break
    gameStep(gallowGrid, mistakes)
    drawGrid()

if winner:
    print("congrats, you won!")
if mistakes == 6:
    print("sorry, you lost!")
            
print('the word was', secretWord)
