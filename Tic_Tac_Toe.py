
#Generating board for game.
GameBoard=[[ "_" for i in range(3)] for j in range(3)]

#Winning condition for the game.
win_pattern = [
    [[1,1], [2,2], [3,3]],  # Diagonal 1
    [[1,3], [2,2], [3,1]],  # Diagonal 2
    [[1,1], [1,2], [1,3]],  # Top row
    [[2,1], [2,2], [2,3]],  # Middle row
    [[3,1], [3,2], [3,3]],  # Bottom row
    [[1,1], [2,1], [3,1]],  # First column
    [[1,2], [2,2], [3,2]],  # Second column
    [[1,3], [2,3], [3,3]]   # Third column
]

#Positions on which "X" is inserted on board.
playerA_positions=[]

#Positions on which "O" is inserted on board.
playerB_positions=[]

#Function for printing the board.
def print_board():
    for row in GameBoard:
        print(row)

#Function for gameplay.
def Game_play():
    for i in range (9):
        if i%2==0:
            result=playerA()
            if result == "won":
                 break
        else:
            result=playerB()
            if result == "won":
                 break
    if result!="won":
        print("Well tried!! Match is tied.Better luck next time ")

#Function for playerA gameplay.
def playerA():
    global pos
    global playerA_positions

    #Taking input from user for player A.
    pos=[input('''Player A:Enter the position for X:)
                  Instructions for input:
                  1.Enter the position as per following manner [Row.No][Column.No]
                    Remember the [] signifies list
                  2.For the reference:
                  ['[1][1]', '[1][2]', '[1][3]']
                  ['[2][1]', '[2][2]', '[2][3]']
                  ['[3][1]', '[3][2]', '[3][3]']
                  
                ''')]
    
    #Checking the input format.
    if len(pos[0]) == 6 and pos[0][0]== '[' and pos[0][2] == ']' and pos[0][3] == '[' and pos[0][5] == ']' and pos[0][1].isdigit() and pos[0][4].isdigit():
         None
    else:
         print('''Invalid input!!!
                  Enter valid position.''')
         return playerA()
    
    #storing the row positon from the input.
    row_pos=int(pos[0][1])

    #storing the column positon from the input.
    col_pos=int(pos[0][4])
    
    #Checking the inserted row position.If its invalid then asking to re-enter.
    if row_pos>3:
         print(f"Player A:Please enter the position of 0 again,You entered invalid position for row position:{row_pos}")
         return playerA() 
    
    #Checking the inserted column position.If its invalid then asking to re-enter.
    elif col_pos>3:
         print(f"Player A:Please enter the position of 0 again,You entered invalid position for column position:{col_pos}")
         return playerA() 
    
    #If the entered position is used before,Asking for a valid position.
    elif ([row_pos,col_pos] in(playerB_positions))or([row_pos,col_pos] in (playerA_positions)):
         print("This position is used before.Please enter the positon again")
         return playerA()
       
    #Inserting the "X" on desired position of board.
    GameBoard[row_pos-1][col_pos-1]="X"

    #Storing the position which used by Player A.
    playerA_positions.append([row_pos,col_pos])

    #Checking for the winning condition.
    if len(playerA_positions)>=3:
        
        for win_list in win_pattern:

            #Checking each winning position with player A positions.
            for win_case in win_list:
                if win_case not in playerA_positions:  
                    break
            else:  
                print("Congratulations!! Player A has won the game.")
                print_board()
                return "won"
            
    print(f"Board after Player A chance:")
    return print_board()

#Function for playerB gameplay.
def playerB():
    global pos
    global playerB_positions

    #Taking input from user for player B.
    pos=[(input('''Player B:Enter the position for O:)
                  Instructions for input:
                  1.Enter the position as per following manner [Row.No][Column.No]
                    Remember the [] signifies list
                  2.For the reference:
                  ['[1][1]', '[1][2]', '[1][3]']
                  ['[2][1]', '[2][2]', '[2][3]']
                  ['[3][1]', '[3][2]', '[3][3]']
                  '''))]
    #Checking the input format.
    if len(pos[0]) == 6 and pos[0][0]== '[' and pos[0][2] == ']' and pos[0][3] == '[' and pos[0][5] == ']' and pos[0][1].isdigit() and pos[0][4].isdigit():
         None
    else:
         print('''Invalid input!!!
                  Enter valid position.''')
         return playerB()
    
    #storing the row positon from the input of position.
    row_pos=int(pos[0][1])

    #storing the column positon from the input of position.
    col_pos=int(pos[0][4])

    #Checking the inserted row position.If its invalid then asking to re-enter.
    if row_pos>3:
            print(f"Player B:Please enter the position of 0 again,You entered invalid position for row position:{row_pos}")
            return playerB()
     
    #Checking the inserted column position.If its invalid then asking to re-enter.
    elif col_pos>3:
            print(f"Player B:Please enter the position of 0 again,You entered invalid position for column position:{col_pos}")
            return playerB() 
    
    #If the entered position is used before,Asking for a valid position.
    elif ([row_pos,col_pos] in(playerB_positions))or([row_pos,col_pos] in (playerA_positions)):
                 print("This position is used before.Please enter the positon again")
                 return playerB()
    
    #Inserting the X on desired position of board.
    GameBoard[row_pos-1][col_pos-1]="O"

    #Storing the position which used by PlayerB.
    playerB_positions.append([row_pos,col_pos])

    #Checking for the winning condition.
    if len(playerB_positions)>=3 :

        #Checking each winning position with player B positions.
        for win_list in win_pattern:
            for win_case in win_list:
                if win_case not in playerB_positions:  
                    break  
            else:
                print("Congratulations!! Player B has won the game.")
                print_board()
                return "won"

    print(f"Board after Player B chance:")
    return print_board()
    
Game_play()

#Asking to play again the game.
def play_again():
     ask=input('''Want to play again??
               Enter Yes or Y to play again.
               Enter No or N for later.
               ''')
     if (ask=="Yes") or (ask=="Y"):
          Game_play()
     elif (ask=="No") or (ask=="N"):
          print("Thanks for playing.Hopefully you enjoyed the game.")
          return None
     else:
          play_again()

play_again()