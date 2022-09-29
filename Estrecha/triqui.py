import random

def drawBoard(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
 

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('¿Quiéres escoger X o O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():

    if random.randint(0, 1) == 0:
        return 'Computador'
    else:
        return 'Usuario'

def makeMove(board, letter, move):
    board[move] = letter


def playAgain():

    print('¿Quiéres jugar otra vez? (si o no)')
    return input().lower().startswith('s')


def isWinner(bo, le):

    return (
    (bo[7] == le and bo[8] == le and bo[9] == le) or # fila superior
    (bo[4] == le and bo[5] == le and bo[6] == le) or # fila del medio
    (bo[1] == le and bo[2] == le and bo[3] == le) or # fila inferior
    (bo[7] == le and bo[4] == le and bo[1] == le) or # columna izquierda
    (bo[8] == le and bo[5] == le and bo[2] == le) or # columna del medio
    (bo[9] == le and bo[6] == le and bo[3] == le) or # columna derecha
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le))   # diagonal

def isSpaceFree(board, move):
   
    return board[move] == ' '

def getPlayerMove(board):
   
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('¿cuál es tu siguiente movimiento? (1-9)')
        move = input()
    return int(move)


def getBoardCopy(board):
   
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard





def chooseRandomMoveFromList(board, movesList):
   
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

