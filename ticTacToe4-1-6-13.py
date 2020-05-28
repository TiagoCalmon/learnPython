from random import randrange

def DisplayBoard(board):
    print("+-------+-------+-------+")
    for i in board:
        print("|       |       |       |")
        print("|   "+str(i[0])+"   |"+"   "+str(i[1])+"   |"+"   "+str(i[2])+"   |" )
        print("|       |       |       |")
        print("+-------+-------+-------+")

    
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#

def EnterMove(board):
    global firstMove, computer, player
    moves = {1 : (0,0), 2 : (0,1), 3 : (0,2), \
             4 : (1,0), 5 : (1,1), 6 : (1,2),\
             7 : (2,0), 8 : (2,1), 9 : (2,2)}
    digit = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    
    while True:
        playerMove = input("Input your move(1-9):  ")
        
        if (playerMove in digit) and (int(playerMove) > 0 or int(playerMove < 10)):
            tmp = moves.get(int(playerMove))
            tmp2 = MakeListOfFreeFields(board)
            if len(tmp2) > 0:
                if tmp in tmp2:
                    board[tmp[0]][tmp[1]] = player
                    return True
                else:
                    print("Input a free slot number!!!")
                    continue
            else:
                #print("Don't have free slot!")
                return False
            print(tmp)
        else:
            if playerMove == "z":
                break
            print("Invalid choice!!! Please, choice a number in [1-9]")
            
    
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields(board):
    #verifica se existe casas livres.
    #Retorna uma lista com tuplas, repesentando linha e coluna das casas livres. 
    #retorna uma lista vazia [] - tamanho zero -se não houver casas livres.
    global computer, player
    aux = []    
    for ix, i in enumerate(board):
        for zx, z in enumerate(i):
            if z != computer and z != player:
                tp = (ix, zx)
                aux.append(tp)
    return aux
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def VictoryFor(board, sign):
    for i in board:
        if i[0] == i[1] == i [2]:
            winner = i[0]
            return winner
    for i in range(3):
        if board[0][i] == board[1][i] ==board[2][i]:
            winner = board[0][i]
            return winner
    if board[0][0] == board[1][1] ==board[2][2]:
        winner = board[0][0]
        return winner
    elif board[0][2] == board[1][1] ==board[2][0]:
        winner = board[0][2]
        return winner
    else:
        return None
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove(board):
    
    global firstMove, computer, player
    if firstMove:
        board[1][1] = computer
        firstMove = False
        return True
    else:
        tmp2 = MakeListOfFreeFields(board)
        if len(tmp2) > 0:
            rnd=randrange(len(tmp2))
            i , j = tmp2[rnd][0], tmp2[rnd][1]
            board[i][j] = computer
            return True
        else:
            return False

#
# the function draws the computer's move and updates the board
#
def test(board):
    ### teste
    #DisplayBoard(board)
    #board[2][0] = computer
    #board[1][0] = computer
    #board[0][0] = computer
    #for i in board:
    #    i[0] = player
    #    i[1] = player
    #    i[2] = player
    #DrawMove(board)
    hasWinner=VictoryFor(board, True)
    freeMoves = MakeListOfFreeFields(board)
    #print(len(freeMoves))
    print(hasWinner)
    DisplayBoard(board)
    DisplayBoard(board)
    EnterMove(board)
    DisplayBoard(board)
    


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
freeMoves = [ (0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2) ]
computer = "X"
player  = "O"
firstMove = True
winner = None
while True:
    if not DrawMove(board):
        winner = None
        break
    DisplayBoard(board)
    winner = VictoryFor(board, True)
    if winner != None:
        break
    if len(MakeListOfFreeFields(board)) == 0:
        winner = None
        break
    if not EnterMove(board):
        winner = None
        break
    winner = VictoryFor(board, True)
    if winner != None:
        break
if winner == None:
    print("It don't have more free Slots!!!")
elif winner == player:
    DisplayBoard(board)
    print(":) YOU WIN!!! ")
elif winner == computer:
    print(":( YOU LOSE!!!")