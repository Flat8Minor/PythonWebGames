import random

board = [['n', 'n', 'n'],['n', 'n', 'n'],['n', 'n', 'n']]
takenSpot = False
invalidAns = False
winnerNC = 'n'

def setup():
    global board, winnerNC
    winnerNC = 'n'
    board = [['n', 'n', 'n'],['n', 'n', 'n'],['n', 'n', 'n']]

def placement(option):
    global takenSpot, board, invalidAns
    takenSpot = False
    invalidAns = False
    option = int(option)
    if (option >= 1) & (option <=3):
            spot = option - 1
            if board[0][spot] == 'n':
                board[0][spot] = 'p'
            else:
                takenSpot = True
    elif (option >= 4) & (option <= 6):
        spot = option - 4
        if board[1][spot] == 'n':
            board[1][spot] = 'p'
        else:
            takenSpot = True
    elif (option >= 7) & (option <= 9):
        spot = option - 7
        if board[2][spot] == 'n':
            board[2][spot] = 'p'
        else:
            takenSpot = True
    else:
        invalidAns = True
    return

def dumbComputer():
    global board
    picking = True
    while picking==True:
        choice=random.randint(1,9)
        if (choice >= 1) & (choice <=3):
            spot = choice - 1
            if board[0][spot] not in ['c','p']:
                    board[0][spot] = 'c'
                    picking = False
                    break
        elif (choice >= 4) & (choice <= 6):
            spot = choice - 4
            if board[1][spot] not in ['c','p']:
                    board[1][spot] = 'c'
                    picking = False
                    break
        elif (choice >= 7) & (choice <= 9):
            spot = choice - 7
            if board[2][spot] not in ['c','p']:
                    board[2][spot] = 'c'
                    picking = False
                    break
    return

def winnerCheck():
    global board, winnerNC
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == board[((i+1) % 3)][((j+1) % 3)]:
                if board[((i+1) % 3)][((j+1) % 3)] == board[((i+2) % 3)][((j+2) % 3)]:
                    if board[((i+2) % 3)][((j+2) % 3)] == board[i][j]:
                        if board[i][j] == 'p':
                            winnerNC = 'p'
                        elif board[i][j] == 'c':
                            winnerNC = 'c'
            elif board[i][j] == board[((i+1)%3)][j]:
                if board[((i+1)%3)][j] == board[((i+2)%3)][j]:
                    if board[((i+2)%3)][j] == board[i][j]:
                        if board[i][j] == 'p':
                            winnerNC = 'p'
                        elif board[i][j] == 'c':
                            winnerNC = 'c'
            elif board[i][j] == board[i][((j+1)%3)]:
                if board[i][((j+1)%3)] == board[i][((j+2)%3)]:
                    if board[i][((j+2)%3)] == board[i][j]:
                        if board[i][j] == 'p':
                            winnerNC = 'p'
                        elif board[i][j] == 'c':
                            winnerNC = 'c'
