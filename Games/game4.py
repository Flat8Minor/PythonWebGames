import random
board4 = [['n','n','n','n','n','n','n'],['n','n','n','n','n','n','n'],['n','n','n','n','n','n','n'],['n','n','n','n','n','n','n'],['n','n','n','n','n','n','n'],['n','n','n','n','n','n','n']]
winnerC4 = 'n'
fullcolumn = False
outOfBounds = False

def cleaning():
    global board4, winnerC4
    winnerC4 = 'n'
    board4 = [['n','n','n','n','n','n','n'],['n','n','n','n','n','n','n'],['n','n','n','n','n','n','n'],['n','n','n','n','n','n','n'],['n','n','n','n','n','n','n'],['n','n','n','n','n','n','n']]

def drop(dropping_area):
    global fullcolumn, board4, outOfBounds
    outOfBounds = False
    fullcolumn = False
    dropping_area = str(dropping_area)
    if dropping_area not in ['1','2','3','4','5','6','7']:
        outOfBounds = True
        return
    else:
        dropping_area = int(dropping_area)
        if (dropping_area < 1) | (dropping_area > 7):
            outOfBounds = True
            return
    dropping_area = dropping_area - 1
    for j in range(5,-2,-1):
        if j == -1:
            fullcolumn = True
            return
        elif board4[j][dropping_area] == 'n':
            board4[j][dropping_area] = 'p'
            return

def computerTurn():
    global board4, fullcolumn
    dropping = True
    while dropping == True:
        dropped=random.randint(0,6)
        for j in range(5,-2,-1):
            if j == -1:
                dropping = True
                break
            elif board4[j][dropped] == 'n':
                board4[j][dropped] = 'c'
                dropping = False
                break
    return

def C4wc():
    global board4, winnerC4
    for j in range(0,4):
        for i in range(0,6):
            if (board4[i][j] == board4[i][(j+1)]):
                if (board4[i][(j+1)] ==  board4[i][(j+2)]):
                    if (board4[i][(j+2)] == board4[i][(j+3)]):
                        if (board4[i][j] == 'p'):
                            winnerC4 = 'p'
                        elif (board4[i][j] == 'c'):
                            winnerC4 = 'c'
        for j in range(0,7):
            for i in range(0,3):
                if (board4[i][j] == board4[(i+1)][j]):
                    if (board4[(i+1)][j] == board4[(i+2)][j]):
                        if (board4[(i+2)][j] == board4[(i+3)][j]):
                            if (board4[i][j] == 'p'):
                                winnerC4 = 'p'
                            elif (board4[i][j] == 'c'):
                                winnerC4 = 'c'
        for j in range(0,4):
            for i in range(3,6):
                if (board4[i][j] == board4[(i-1)][(j+1)]):
                    if (board4[(i-1)][(j+1)] == board4[(i-2)][(j+2)]):
                        if (board4[(i-2)][(j+2)] == board4[(i-3)][(j+3)]):
                            if (board4[i][j] == 'p'):
                                winnerC4 = 'p'
                            elif (board4[i][j] == 'c'):
                                winnerC4 = 'c'
        for j in range(3,7):
            for i in range(3,6):
                if (board4[i][j] == board4[(i-1)][(j-1)]):
                    if (board4[(i-2)][(j-2)] == board4[(i-1)][(j-1)]):
                        if (board4[(i-2)][(j-2)] == board4[(i-3)][(j-3)]):
                            if (board4[i][j] == 'p'):
                                winnerC4 = 'p'
                            elif (board4[i][j] == 'c'):
                                winnerC4 = 'c'
