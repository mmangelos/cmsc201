# File:        proj2.py
# Author:      Mitchell Angelos
# Date:        4/18/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: 
#   This program is a version of the game Reversi.

# printing board
TURN_X = "X" # player
TURN_O = "O" # CPU
EMPTY_SPACE = "_"
BORDER_CHAR = "|"
BOARD_LENGTH = 8
CURRENT_BOARD_STR = "Current board state: "
BOARD_HEADER = "_|0|1|2|3|4|5|6|7"
INITIAL_COORD_X = 3
INITIAL_COORD_Y = 3
END_INIT_COORD = 5

# directions
D_UP = "UP"
D_DOWN = "DOWN"
D_LEFT = "LEFT"
D_RIGHT = "RIGHT"
DIRECTION_INDEX = 2

# move
GET_MOVE = "Please enter a valid move: "
VALID_MOVES_FOLLOW = "Here are your valid moves: "
MOVE_IS_INVALID = "The move you just entered is not valid. Valid moves are: "
FIRST_NUM_PLACE = 0
SECOND_NUM_PLACE = 2
MAX_MOVE_LEN = 3
SPACE_INDEX = 1

# prominent strings
SPACE_KEY = " "
GAME_OVER = "GAME OVER!"
CPU_TAKES_MOVE = "CPU takes move:"
PLAYER_SCORE = "Player score:"
COMPUTER_SCORE = "Computer score:"
WINS_STR = " wins!"

#####################################################################
# createBoard() creates the Reversi board filled with empty spaces
# Parameters:   None
# Output:       board; the 2D list containing the new, clean board
def createBoard():

    board = []

    for i in range(0, BOARD_LENGTH, 1):
        # adds a row
        board.append([])
        # shallow copy of that created row
        tempList = board[i]
        for j in range(0, BOARD_LENGTH, 1):
            # adds an empty space
            tempList.append(EMPTY_SPACE)

    # adds the initial x's and o's in the middle of the board
    addInitialTurns(board)
            
    return board

#############################################################################
# setCoordinates() sets a coordinate on the Reversi board to a certain symbol
# Parameters:      x; the row to access
#                  y; the column to access
#                  turn; the symbol to set this coordinate to
#                  board; the current Reversi board
# Output:          None
def setCoordinates(x, y, turn, board):

    # since board is mutable, no return needed
    # at this coordinate on the board, set the symbol
    board[x][y] = turn

#####################################################################
# setTurn()   sets the symbol to the opposite symbol
# Parameters: currentTurn; the current symbol
# Output:     the opposite turn
def setTurn(currentTurn):

    # if the turn is x, it changes the turn to o
    if currentTurn == TURN_X:
        return TURN_O
    # if the turn is o, it changes the turn to x
    elif currentTurn == TURN_O:
        return TURN_X

#####################################################################
# addInitialTurns() a helper function that adds the four initial
#                   symbols to the middle of the board
# Parameters:       board; the current Reversi board
# Output:           None
def addInitialTurns(board):

    turn = TURN_X
    # indexing starts at x position of the initial x at (3,3)
    for i in range(INITIAL_COORD_X, END_INIT_COORD, 1):
        # sets the first smybol on that row
        setCoordinates(i, INITIAL_COORD_Y, turn, board)
        # sets the turn
        turn = setTurn(turn)
        # sets the second symbol on that row
        setCoordinates(i, INITIAL_COORD_Y + 1, turn, board)

#####################################################################
# printBoard() prints the Reversi board with the right headings
# Parameters: board; a 2D list of single-char strings (X, O, _)
# Output:     None
def printBoard(board):

    print(CURRENT_BOARD_STR)
    # print header
    print(BOARD_HEADER)
    # prints each row
    for i in range(len(board)):
        print(str(i) + BORDER_CHAR + BORDER_CHAR.join(board[i]) + \
              BORDER_CHAR)

####################################################################
# returnMoves() gets the valid moves able to be played
# Parameters:   board; the current Reversi board
#               turn; the symbol to be checking valid turns for
#               oppTurn; the opposite symbol
# Return:       a list of valid moves
def returnMoves(board, turn, oppTurn):
    
    moves = []

    # iterates through the entire board
    for i in range(len(board)):
        for j in range(len(board[i])):
            
            # if that spot on the board is an empty space
            if board[i][j] == EMPTY_SPACE:
                # checking a row TO THE RIGHT
                nextToOpp = False # is the turn next to the opposite turn
                hasSpace = False # used for checking if valid
                direcUsed = False # if this direction already's used
                # if next place is out of bounds, do nothing
                if j + 1 != len(board[i]):
                    # ...it checks if the opposite turn is next to it...
                    if board[i][j + 1] == oppTurn:
                        nextToOpp = True
                    # ...and if it is, it will check if it is sandwiched...
                    if nextToOpp == True:
                        for l in range(j + 1, len(board[i])):
                            if board[i][l] == EMPTY_SPACE:
                                hasSpace = True # there's a space, so you
                                # cannot play here
                            elif board[i][l] == turn:
                                # ...and if it finds that it is sandwiched,
                                # it'll say that place is a valid move.
                                # (also checks if is duplicate)
                                if [i, j] not in moves and hasSpace != True:
                                    moves.append([i, j])
                                    moves.append([[D_RIGHT, l]])
                                    direcUsed = True
                                    # this is set to true to show that this
                                    # direction is already used, so we cannot
                                    # use it again.
                                elif [i, j] in moves and hasSpace != True and \
                                     direcUsed == False:
                                    # this move already exists, but uses a
                                    # different direction, so we add the
                                    # direction it also needs to flip here
                                    for a in range(len(moves)):
                                        if moves[a] == [i, j]:
                                            moves[a + 1].append([D_RIGHT, l])
                                        
                # The rest of these follow the same principal, just
                # checking in different directions
                                            
                # checks to the left, follows same code as above
                nextToOpp = False
                hasSpace = False
                direcUsed = False
                if j - 1 != -1:
                    if board[i][j - 1] == oppTurn:
                        nextToOpp = True
                    if nextToOpp == True:
                        # instead of scanning to right, this for loop
                        # starts from the right and scans left.
                        for k in range(j - 1, -1, -1):
                            if board[i][k] == EMPTY_SPACE:
                                hasSpace = True
                            elif board[i][k] == turn:
                                if [i, j] not in moves and hasSpace != True:
                                    moves.append([i, j])
                                    moves.append([[D_LEFT, k]])
                                    direcUsed = True
                                elif [i, j] in moves and hasSpace != True and \
                                     direcUsed == False:
                                    for b in range(len(moves)):
                                        if moves[b] == [i, j]:
                                            moves[b + 1].append([D_LEFT, k])

                # checks up above
                nextToOpp = False
                hasSpace = False
                direcUsed = False
                if i - 1 != -1:
                    if board[i - 1][j] == oppTurn:
                        nextToOpp = True
                    if nextToOpp == True:
                        for x in range(i - 1, -1, -1):
                            if board[x][j] == EMPTY_SPACE:
                                hasSpace = True
                            elif board[x][j] == turn:
                                if [i, j] not in moves and hasSpace != True:
                                    moves.append([i, j])
                                    moves.append([[D_UP, x]])
                                    direcUsed = True
                                elif [i, j] in moves and hasSpace != True and \
                                     direcUsed == False:
                                    for c in range(len(moves)):
                                        if moves[c] == [i, j]:
                                            moves[c + 1].append([D_UP, x])

                # checks under
                nextToOpp = False
                hasSpace = False
                direcUsed = False
                if i + 1 != len(board):
                    if board[i + 1][j] == oppTurn:
                        nextToOpp = True
                    if nextToOpp == True:
                        for c in range(i + 1, len(board)):
                            if board[c][j] == EMPTY_SPACE:
                                hasSpace = True
                            elif board[c][j] == turn:
                                if [i, j] not in moves and hasSpace != True:
                                    moves.append([i, j])
                                    moves.append([[D_DOWN, c]])
                                    direcUsed = True
                                elif [i, j] in moves and hasSpace != True and \
                                     direcUsed == False:
                                    for d in range(len(moves)):
                                        if moves[d] == [i, j]:
                                            moves[d + 1].append([D_DOWN, c])
                                            
    # returns valid moves calculated by the algorithm.
    return moves

###################################################################
# getChoices() condensces the information from returnMoves() for easy checks
# Parameters:  validMoves; a list full of the valid moves
# Output:      a list full of ONLY coordinates of valid moves
def getChoices(validMoves):

    tempList = [] # stores move in here
    print(VALID_MOVES_FOLLOW, end="")
    for i in range(0, len(validMoves), 2):
        # adds move to the list, skipping the parts of the validMoves list
        # where it stores directions for said moves
        tempList.append(validMoves[i])
    return tempList
        

####################################################################
# getMove()   gets the move the user wants to play
# Parameters: validMoves; the valid moves the user can take
# Output:     a list consisting of the coordinates to play and other info
def getMove(validMoves):
    
    move = ""
    choices = getChoices(validMoves) # gets the choices for moves
    doNotDupe = []
    for x in range(len(choices)):
        if choices[x] not in doNotDupe:
            # appends non-duplicate moves so the user can see them
            doNotDupe.append(choices[x])
    print(doNotDupe)
    # while the user does not give a valid move
    while move not in choices:
        move = input(GET_MOVE) # gets the user's move
        # if the input has the correct formatting...
        if len(move) == MAX_MOVE_LEN and move[SPACE_INDEX] == SPACE_KEY:
            # ...it creates a list with the move...
            move = [int(move[FIRST_NUM_PLACE]), int(move[SECOND_NUM_PLACE])]
            # ...and if that move is not a valid move...
            if move not in choices:
                #...it says it's not a valid move and prints the valid choices
                print(MOVE_IS_INVALID + str(choices))
        else:
            # if the move FORMATTING (i.e. how it was typed in) was not
            # valid, it says the move isn't valid and prints valid choices
            print(MOVE_IS_INVALID + str(choices))

    # this just finds the directions for that move so pieces can be flipped
    indexes = []
    for i in range(0, len(validMoves), 2):
        if move == validMoves[i]:
            indexes.append(validMoves[i + 1])

    # the move and the directions needed for flipping is returned
    return move + [indexes]
    
####################################################################
# flipPieces() flips the necessary pieces on the board
# Parameters:  board; the current Reversi board
#              turn; the current turn
#              oppTurn; the opposite turn
#              move; a list with the move coordinates and extra info
# Output:      None
def flipPieces(board, turn, oppTurn, move):
    
    direcs = 0 # list that stores direction and stopping place
    end = 0 # stopping place

    for x in range(len(move[DIRECTION_INDEX][0])):
        direcs = move[DIRECTION_INDEX][0] # finds list where direction's stored
        end = direcs[x][1] # finds the end 

        # flips pieces going downward
        if direcs[x][0] == D_DOWN:
            for i in range(move[0], end):
                board[i][move[1]] = turn
        # flips pieces going upward
        if direcs[x][0] == D_UP:
            for j in range(end, move[0]):
                board[j][move[1]] = turn
        # flips pieces going right
        if direcs[x][0] == D_RIGHT:
            for k in range(move[1], end):
                board[move[0]][k] = turn
        # flips pieces going left
        if direcs[x][0] == D_LEFT:
            for l in range(end, move[1]):
                board[move[0]][l] = turn

####################################################################
# playComputerMove() plays the computer's move
# Parameters:        board; the current Reversi board
#                    moves; the valid moves for the computer
# Output:            if the cpu has no valid moves, it returns false
def playComputerMove(board, moves):

    # if the cpu has no valid moves,
    # the cpu has lost.
    if len(moves) == 0:
        return False
    
    storeIndex = 0
    minX = moves[0][0]
    minY = moves[0][1]
    # checks every valid move that the CPU has
    for i in range(0, len(moves), 2):
        # the row CAN be equal, but the column MUST NOT be
        if moves[i][0] <=  minX and moves[i][1] < minY:
            minX = moves[i][0]
            minY = moves[i][1]
            storeIndex = i
    # sets the coordinate of the computer's play
    setCoordinates(moves[storeIndex][0], moves[storeIndex][1], TURN_O, board)
    # flips cpu's pieces
    theMove = moves[storeIndex] + [[moves[storeIndex + 1]]] # the cpu's move
    flipPieces(board, TURN_O, TURN_X, theMove)
    print(CPU_TAKES_MOVE, str([moves[storeIndex][0], moves[storeIndex][1]]))

#######################################################################
# endGame()   Ends the game and prints the results
# Parameters: board; the current Reversi board
#             winner; the winner's symbol
# Output:     None
def endGame(board, winner):
    playerScore = 0 # the player's final score
    computerScore = 0 # the cpu's final score
    # goes through the entire board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == TURN_X:
                playerScore += 1 # adds 1 to player score if that piece = x
            elif board[i][j] == TURN_O:
                computerScore += 1 # adds 1 to cpu score if that piece = o
    print(GAME_OVER) # prints game over
    printBoard(board) # draws the board
    print(PLAYER_SCORE, str(playerScore)) # prints the player's score
    print(COMPUTER_SCORE, str(computerScore)) # prints the cpu's score
    print(winner + WINS_STR) # prints who wins
    
def main():

    board = createBoard() # creates the game board
    winner = EMPTY_SPACE # sets winner to an empty space (placeholder)
    # while a winner has not been chosen
    while winner == EMPTY_SPACE:
        printBoard(board) # prints the board
        # gets the move from the user and places it on the board
        valMoves = returnMoves(board, TURN_X, TURN_O)
        # if the player has no valid moves, the player has lost
        if len(valMoves) == 0:
            winner = TURN_O # sets winner to O (CPU)
        else:
            # gets the player's valid move they want to play
            move = getMove(valMoves)
            flipPieces(board, TURN_X, TURN_O, move) # flips
            setCoordinates(move[0], move[1], TURN_X, board) # plays the move
            # checks if the cpu has lost, if it hasn't it plays its move
            if playComputerMove(board, returnMoves(board, TURN_O, TURN_X)) \
               == False:
                winner = TURN_X # sets winner to X (PLAYER)
    endGame(board, winner) # ends the game

main()
