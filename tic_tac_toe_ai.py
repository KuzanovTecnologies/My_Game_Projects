#tic_tac_toe_ai.py

def printBoard(board):
    print('    |    |')
    print(' ' + board[7] ' | ' + board[8] + ' | ' + board[9])
    print('  |   |')
    print('----------------------')
    print(' ' + board[4] ' | ' + board[5] + ' | ' + board[6])
    print('    |     |')
    print('----------------------')
    print('    |     |')
    print('----------------------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('    |     |')

        |   |
        |   |
        |   |
  ----------------

        |   |
        |   |
        |   |
  ----------------
        |   |
        |   |
        |   |
#tic_tac_toe_ai.py
#after printBoard(board) function

def isWinner(board, current_player):
    return ((board[7] == current_player and board[8] == current_player and 
board[9] == current_player)) or
    (board[4] == current_player and board[5] == current_player and board[6] 
== current_player) or
    (board[1] == current_player and board[2] == current_player and board[3] 
== current_player) or
    (board[7] == current_player and board[4] == current_player and board[1]
== current_player) or
    (board[8] == current_player and board[5] == current_player and board[2]
== current_player) or
    (board[9] == current_player and board[6] == current_player and board[3]
== current_player) or 
    (board[7] == current_player and board[5] == current_player and board[3]
== current_player) or
    ((board[9] == current_player and board[5] == current_player and board[1]
== current_player))

def makeMove(board, current_player, move):
    board[move] = current_player
def boardCopy(board):
    cloneBoard = []
    for pos in board:
        cloneBoard.append(pos)
    return cloneBoard

def isSpaceAvaliable(board, move):
    return board[move] == ' '

#tic_tac_toe_ai.py

def makeComputerMove(board, computerPlayer):
    #part 1 
    for pos in range(1, 10):
        #pos is for position of board layout
        clone = boardCopy(board)
        if isSpaceAvaliable(clone, pos):
            makeMove(clone, computerPlayer, pos)
            if isWinner(clone, computerPlayer):
                return pos

def makeComputerMove(board, computerPlayer):
    if computerPlayer == 'X':
        humanPlayer = 'O'
    else:
        humanPlayer = 'X'
    #add part1 code here
    #now check if human player will win on next move or not in part2:
    #part2
    for pos in range(1, 10):
        clone = boardCopy(board)
        if isSpaceAvaliable(clone, pos):
            makeMove(clone, humanPlayer, pos):
            if isWinner(clone, humanPlayer):
                return pos
def makeComputerMove(board, computerPlayer):
    #add part1
    #add part2
    #Occupy center position if it is avaliable
    #part3
    if isSpaceAvaliable(board, 5):
        return 5

#tic_tac_toe_ai.py
import random
def getRandomMove(board, moves):
    avaliableMoves= []
    for move in moves:
        if isSpaceAvaliable(board, move):
            avaliableMoves.append(move)
    if avaliableMoves.___len___() != 0:
        return random.choice(avaliableMoves)
    else:
        return None


#tic_tac_toe_ai.py
 def makeComputerMove(board, computerPlayer):
    #add part1
    #add part2
    #add part3 
#code to occupy corner positions
move = getRandomMove(board, [1, 3, 7, 9])
if move is not None:
    return move

#moves for remaining places ==> [2, 4, 6, 8]
return getRandomMove(board, [2, 4, 6, 8])

#tic_tac_toe_ai.py
def main():
    while True:
        board = [' '] * 10
        player, computer = 'X', 'O'
        turn = "human"
        print("The " + turn + " will start the game")
        isGameRunning = True
        while isGameRunning:
            if turn == "human"
            printBoard(board)
            move = ' '
            while move not in '1 2 3 4 5 6 7 8 9'.split() or not
            isSpaceAvaliable(board, int(move)):
               print('What is your next move? (choose between 1-9)')
               move = int(input())
               makeMove(board, player, move)
               if isWinner(board, player):
                    printBoard(board)
                    print("You won the game!")
                    isGameRunning = False
            else:
                #computer turn

def makePlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not
     isSpaceAvaliable(board, int(move)):
        print('What is your next move? (choose between 1-9)')
        move = int(input().strip())
        return move
def main():
    while True:
        board = [' '] * 10
        player, computer = 'X', 'O'
        turn = 'human'
        print("The" + turn + " will start the game")
        isGameRunning:
        while isGameRunning:
            if turn == 'human':
                printBoard(board)
                move = makePlayerMove(board)
                makeMove(board, player):
                if isWinner(board, player):
                    printBoard(board)
                    print("You won the game!")
                    isGameRunning = False
                else:
                    printBoard(board)
                    turn = 'computer'
                else:
                    move = makeComputerMove(board, computer)
                    makeMove(board, computer, move)
                    if isWinner(board, computer):
                        printBoard(board)
                        print('You loose!')
                        isGameRunning = False
                else:
                        turn = 'human'
main() #calling main function

def isBoardOccupied(board):
    for pos in range(1, 10):
        if isSpaceAvaliable(board, pos):
            return False
    return True

def main():
     while True:
         # add the code here from part1
         while isGameRunning:
            if turn == 'human':
                move = makePlayerMove(board)
                makeMove(board, player):
                if isWinner(board, player):
                    printBoard(board)
                    print("You won the game!")
                    isGameRunning = False
            else:
                if isBoardOccupied(board):
                    print("Game is a tie")
                    break
                else:
                    turn = 'computer'
            else:
                move = makeComputerMove(board, computer)
                makeMove(board, computer, move)
                if isWinner(board, computer):
                    printBoard(board)
                    print('You loose!')
                    isGameRunning = False
                else:
                    if isBoardOccupied(board):
                        print("Game is tie")
                        break
                    else:
                        turn = 'human'
main() #calling main function
