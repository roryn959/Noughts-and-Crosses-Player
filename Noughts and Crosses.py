#Noughts and Crosses
#Minimax algorithm practice
import time, random, math
global possibleMoves, boardP, iterations
iterations = 0

def Main():
    print("Player = X\nCPU = O\n")
    PrintBoard(boardP)
    complete = False
    if random.randint(0, 1) == 0:
        Player_Turn()
    while complete == False:
        if len(possibleMoves) == 0:
            break
        print("\n*CPU's turn*\n")
        CPU_Turn()
        if CheckWin(boardP) == 10:
            complete == True
            print("CPU wins")
            break
        elif CheckWin(boardP) == 'Draw':
            complete = True
            print("Draw!")
        else:
            Player_Turn()
            if CheckWin(boardP) == -10:
                complete = True
                print("Player wins!\n")
            elif CheckWin(boardP) == 'Draw!':
                complete = True
                print("Draw!\n")
            
def Player_Turn():
    global possibleMoves, boardP
    valid = False
    while valid == False:
        print("\n{0}".format('/'.join(possibleMoves)))
        choice = input("\nPlease enter a choice from the positions above: ")
        choice = choice.upper()
        if not(choice in possibleMoves):
            print("Invalid choice. Please try again.\n")
        else:
            valid = True
    boardP = RegChoice('X', choice, boardP)
    possibleMoves.remove(choice)
    PrintBoard(boardP)

def RegChoice(s, choice, board):
    boardx = board.copy()
    if choice == 'TL':
        boardx[0] = s
    elif choice == 'TC':
        boardx[1] = s
    elif choice == 'TR':
        boardx[2] = s
    elif choice == 'ML':
        boardx[3] = s
    elif choice == 'MC':
        boardx[4] = s
    elif choice == 'MR':
        boardx[5] = s
    elif choice == 'BL':
        boardx[6] = s
    elif choice == 'BC':
        boardx[7] = s
    elif choice == 'BR':
        boardx[8] = s
    else:
        print("Error 1", choice)
    return boardx

def CPU_Turn():
    global possibleMoves, boardP, iterations
    start_time = time.perf_counter()
    #choice = Alphabeta(boardP.copy(), possibleMoves.copy(), -(math.inf), math.inf, 1, 0)[0]
    choice = Minimax(boardP.copy(), possibleMoves.copy(), 1)[0]
    boardP = RegChoice('O', choice, boardP)
    PrintBoard(boardP)
    end_time = time.perf_counter()
    exec_time = end_time-start_time
    print("\nFinished turn in", exec_time, "seconds, processing", iterations, "iterations.\n")
    iterations = 0
    possibleMoves.remove(choice)

def Minimax(newBoard, newPosMoves, player): #Player 1 = CPU. Player 0 = Player
    global iterations
    iterations = iterations+1
    if player == 1:
        best = [None, -(math.inf)] #Best = [Move, best value]
    else:
        best = [None, math.inf]
        
    if CheckWin(newBoard) == -10:
        return [None, -10]
    elif CheckWin(newBoard) == 10:
        return [None, 10]
    elif CheckWin(newBoard) == 'Draw':
        return [None, 0]

    if player == 1:
        for i in range(0, len(newPosMoves)):
            x = RegChoice('O', newPosMoves[i], newBoard)
            k = Minimax(x, Remover(newPosMoves, newPosMoves[i]), 0) #k = [None, value of move made]
            k[0] = newPosMoves[i]
            if k[1]>best[1]:
                best = k
                
    elif player == 0:
        for i in range(0, len(newPosMoves)):
            x = RegChoice('X', newPosMoves[i], newBoard)
            k = Minimax(x, Remover(newPosMoves, newPosMoves[i]), 1)
            k[0] = newPosMoves[i]
            if k[1]<best[1]:
                best = k
    return best                  

def Alphabeta(newBoard, newPosMoves, alpha, beta, player, depth):
    global iterations
    iterations = iterations+1
    if player == 1:
        best = [None, -(math.inf)] #Best = [Move, best value]
    else:
        best = [None, math.inf]
        
    if CheckWin(newBoard) == -10:
        return [None, -10-depth]
    elif CheckWin(newBoard) == 10:
        return [None, 10-depth]
    elif CheckWin(newBoard) == 'Draw':
        return [None, 0-depth]

    if player == 1:
        for i in range(0, len(newPosMoves)):
            x = RegChoice('O', newPosMoves[i], newBoard)
            k = Alphabeta(x, Remover(newPosMoves, newPosMoves[i]), alpha, beta, 0, depth+1) #k = [Move, value of move made]
            k[0] = newPosMoves[i]
            if k[1]>best[1]:
                best = k
            alpha = max(alpha, k[1])
            if beta <= alpha:
                break
                
    elif player == 0:
        for i in range(0, len(newPosMoves)):
            x = RegChoice('X', newPosMoves[i], newBoard)
            k = Alphabeta(x, Remover(newPosMoves, newPosMoves[i]), alpha, beta, 1, depth+1)
            k[0] = newPosMoves[i]
            if k[1]<best[1]:
                best = k
            beta = min(beta, k[1])
            if beta <= alpha:
                break
    return best  

def Remover(lista, item):
    listc = lista.copy()
    listc.remove(item)
    return listc

def PrintBoard(board):
    print(f"---------\n{board[0]} | {board[1]} | {board[2]}\n   ---\n{board[3]} | {board[4]} | {board[5]}\n   ---\n{board[6]} | {board[7]} | {board[8]}\n---------")

def CheckWin(board):
    if (board[0] == 'X' and board[1] == 'X' and board[2] == "X") or  (board[3] == 'X' and board[4] == 'X' and board[5] == "X") or (board[6] == 'X' and board[7] == 'X' and board[8] == "X") or (board[0] == 'X' and board[3] == 'X' and board[6] == "X") or (board[1] == 'X' and board[4] == 'X' and board[7] == "X") or (board[2] == 'X' and board[5] == 'X' and board[8] == "X") or (board[0] == 'X' and board[4] == 'X' and board[8] == "X") or (board[2] == 'X' and board[4] == 'X' and board[6] == "X"):
        return -10    
    elif (board[0] == 'O' and board[1] == 'O' and board[2] == "O") or (board[3] == 'O' and board[4] == 'O' and board[5] == "O") or (board[6] == 'O' and board[7] == 'O' and board[8] == "O") or (board[0] == 'O' and board[3] == 'O' and board[6] == "O") or (board[1] == 'O' and board[4] == 'O' and board[7] == "O") or (board[2] == 'O' and board[5] == 'O' and board[8] == "O") or (board[0] == 'O' and board[4] == 'O' and board[8] == "O") or (board[2] == 'O' and board[4] == 'O' and board[6] == "O"):
        return 10
    elif CheckSpaces(board) == False:
        return 'Draw'

def CheckSpaces(board):
    spaces = False
    for i in range(0, len(board)):
        if " " in board[i]:
            spaces = True
    return spaces

possibleMoves = ["TL", "TC", "TR", "ML", "MC", "MR", "BL", "BC", "BR"]
boardP = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
Main()

while True:
    again = input("\nPlay again? Y/N")
    if again.lower() == 'n':
        break
    else:
        possibleMoves = ["TL", "TC", "TR", "ML", "MC", "MR", "BL", "BC", "BR"]
        boardP = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        print('')
        Main()
