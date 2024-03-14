import TicTacToe_resultCheck
import math

m = 0
n = 0
isMaximizing = True
x = 'X'
o = 'O'

def Input():
    global m
    m = int(input("Tong so nuoc da di (m >= 0): "))
    global n
    n = int(input("Kich thuoc ban co (10 < n < 20): "))
    

    checkInput(m, n)


def checkInput(m, n):
    if m < 0 or n <= 1 or n >= 9:
        print("")
        print("Nhap lai input!")
        Input()
    else:
        preMove(m, n)
    
    
def preMove(m, n):
    print("")
    print("Chương trình được code cho X đi trước và lượt cần xác định là lượt của X.")
    
    board = ['-']*(n*n)
    
    for i in range(m):
        x1, y1 = input("Nhap toa do nuoc di: ").split()
        x1 = int(x1)
        y1 = int(y1)
        
        if i % 2 == 0 or i == 0:
            board[x1*n + y1] = x
            displayBoard(board, n)
        else:
            board[x1 * n + y1] = o
            displayBoard(board, n)
    bestMove(board, n)
    
                
   
def displayBoard(board, n):
    for i in range(0, len(board), n):
        values = [str(z[0]) for z in board[i:i+n]]
        print(' '.join(values))

 
 
def bestMove(board, n):
    check1 = 0
    check2 = 0
    bestScore = -(math.inf)
    global isMaximizing
    
    for l in range(n):
        for k in range(n):
            if board[l * n + k] == '-':
                board[l * n + k] = x
                score = minimax(board, 0, isMaximizing)
                board[l * n + k] = '-'
                bestScore = max(score, bestScore) 
                check1 = l
                check2 = k
      
    print(check1)
    print(check2 + 1)
    
                
 
 
def minimax(board, depth, isMaxing):
    result = TicTacToe_resultCheck.checkState(board, n)
    if result != None:
        return result
    
    bestScore = -(math.inf)
    
    if isMaxing == True:
        bestScore = -(math.inf)
        for l in range(n):
            for k in range(n):
                if board[l * n + k] == '-':
                    board[l * n + k] = x
                    score = minimax(board, depth + 1, False)
                    bestScore = max(score, bestScore) 
        return bestScore
    else:
        bestScore = math.inf
        for l in range(n):
            for k in range(n):
                if board[l * n + k] == '-':
                    board[l * n + k] = o
                    score = minimax(board, depth + 1, True)
                    bestScore = min(score, bestScore) 
        return bestScore
 
            
def play():    
    Input()    
    
# Start 
play()
