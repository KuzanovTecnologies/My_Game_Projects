#filename: conditionals.py

if (True):
  #Do something

if type(item) != int:
         break
else:
         refined_items.append(item)
[1,5,7,8]

#code is written in same previous file

choices = []
for pos in range(0,9):
      choices.append(str(pos+1))
#board layout
print('\n')
print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
print('-----------')
print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
print('-----------')
print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')

#output
'''
|1|2|3|
------------
|4|5|6|
------------
|7|8|9
'''

while True:
    print('\n')
    print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print('-----------')
    print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print('-----------')
    print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    #above code is to print board layouts

    try:
        choice = int(input("> ").strip())
    except:
        print("Please enter only valid fields from board (0-8)")
        continue
    #creating Boolean variable
    Is_current_One = True #default player is player X

    #first move is done by player X
    while True:
        #put code of board layouts here
        if Is_current_One
            print("Player X")
        else:
            print("Player O")
        #put try and except block here
        #---------------------------------------------
        #code to put either X or O on position selected by user
        if Is_Current_One:
            choices[choice-1] = 'X'
        else:
            choices[choice-1] = 'O'
        #code to toggle between True and False
        Is_Current_One = not Is_Current_One
| 1 | 2 | 3 |
  ----------
| 4 | 5 | 6 |
  ----------
| 7 | 8 | 9 |

won = False #at first we don't have any winner
while not won:
    #code from previous topics
    #logic to make any player winner:
    for pos_x in range(0,3):
        pos_y = pos_x * 3

    #for row condition:
    if (choices[pos_y] == choices[(pos_y + 1)] and (choices[pos_y]
    == choices[(pos_y + 2)])):
    #code to change won to True
    won = True #main loop will break
#column condition:
if (choices[pos_x] == choices[(pos_x + 3)]) and (choices[pos_x]
== choices[(pos_x + 6)]):
  won = True #main loop will break
while not won:
    #code from previous topic
    for pos_x in range(0,3):
        pos_y = pos_x * 3
    #add condition for row and column here

#print who is winner
print("Player " + str(int(Is_Current_One + 1)) + " won, Congratulations!")

while not won:
    #code from previous topic
    for pos_x in range(0,3):
        pos_y = pos_x * 3
    #add condition for row and column here

    #diagonal condition here:
    if ((choices[0] == choices[4] and choices[0] == choices[8])) or
       ((choices[2] == choices[4] and choices[4] == choices[6])):

       won = True

#print who is winner
print("Player " + str(int(Is_Current_One + 1)) + " won, Congratulations!")

