n = int(input("Enter any number:"))
for i in range(1, 100):
    if i == n:
        print(i)
        break
def fun(b):
    print("message")
    a = 9 + b
    move_player(a)

fun(3)

#This code is written as scripts
game_board = ['_'] * 9 #this will create 9 underscores
print(game_board[0] + '|' + game_board[1] + '|' + game_board[2])
print(game_board[3] + '|' + game_board[4] + '|' + game_board[5])
print(game_board[6] + '|' + game_board[7] + '|' + game_board[8])
game_board = ['_'] * 9
print(game_board[0] + '|' + game_board[1] + '|' + game_board[2])
print(game_board[1] + '|' + game_board[4] + '|' + game_board[5])
print(game_board[6] + '|' + game_board[7] + '|' + game_board[8])

#output
"""
    _ | _ | _ 
    _ | _ | _
    _ | _ | _
"""

#code from models

#.............................................................................

#code for user input

while True:
     pos = input("Enter any position you want from (0-8): \n")
     pos = int(pos)
     game_board(pos) = 'X'
     print(game_board[0] + '|' + game_board[1] + '|' + game_board[2])
     print(game_board[3] + '|' + game_board[4] + '|' + game_board[5])
     print(game_board[6] + '|' + game_board[7] + '|' + game_board[8])

