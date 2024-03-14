def checkState(board, n):
    return checkDiag(board, n)
    
    
    
def checkDiag(board, n):
    #Check first diagonal line.
    j1 = 0
    j2 = 0
    for i in range(n - 1):
        if board[i * n + i] == board[(i + 1) * (n + 1)] and board[i * n + i] == 'X' and board[(i + 1) * (n + 1)] == 'X':
            j1 = j1 + 1
    if j1 + 1 == n:
        # finalState('X', 1)
        return 1

    
    
    for i in range(n - 1):
        if board[i * n + i] == board[(i + 1) * (n + 1)] and board[i * n + i] == 'O' and board[(i + 1) * (n + 1)] == 'O':
            j2 = j2 + 1
    if j2 + 1 == n:
        # finalState('O', 2)
        return -1

    
    #Check second diagonal line.
    k1 = 0
    k2 = 0
    for i in range(n - 1):
        if board[(i + 1) * (n - 1)] == board[(i + 2) * (n - 1)] and board[(i + 1) * (n - 1)] == 'X' and board[(i + 2) * (n - 1)] == 'X':
            k1 = k1 + 1
    if k1 + 1 == n:
        # finalState('X', 3)
        return 1

    
    for i in range(n - 1):
        if board[(i + 1) * (n - 1)] == board[(i + 2) * (n - 1)] and board[(i + 1) * (n - 1)] == 'O' and board[(i + 2) * (n - 1)] == 'O':
            k2 = k2 + 1
    if k2 + 1 == n:
        # finalState('O', 4)
        return -1

    
    
    return checkCol(board, n)



def checkCol(board, n):
    i = 0
    j = 0
    for k in range(n):
        for l in range(n - 1):
            if board[l * n + k] == board[(l + 1) * n + k] and board[l * n + k] == 'X' and board[(l + 1) * n + k] == 'X':
                i = i + 1
            if board[l * n + k] == board[(l + 1) * n + k] and board[l * n + k] == 'O' and board[(l + 1) * n + k] == 'O':
                j = j + 1
        if i + 1 == n:
            # finalState('X', 5)
            return 1
        elif j + 1 == n:
            # finalState('O', 6)
            return -1
        else:
            i = 0
            j = 0

         
    return checkRow(board, n)
     
            
def checkRow(board, n):
    i = 0
    j = 0
    for l in range(n):
        for k in range(n - 1):
            if board[l * n + k] == board[l * n + 1 + k] and board[l * n + k] == 'X' and board[l * n + 1 + k] == 'X':
                i = i + 1
            if board[l * n + k] == board[l * n + 1 + k] and board[l * n + k] == 'O' and board[l * n + 1 + k] == 'O':
                j = j + 1
        if i + 1 == n:
            # finalState('X', 7)
            return 1

        elif j + 1 == n:
            # finalState('O', 8)
            return -1
        else:
            i = 0
            j = 0
        
    return checkTie(board, n)


def checkTie(board, n):
    if '-' not in board:
        # finalState(n, 9)
        return 0

        
# def finalState(n, z):
#     if z != 9:
#         return 'winner'
#     if z == 9:
#         return 'tie'
