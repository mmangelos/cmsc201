# File:        proj3.py
# Author:      Mitchell Angelos
# Date:        5/8/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: 
#     A program of a game of Minesweeper. Includes some recursion, mutliple
#     2D lists, and application of computer science principles and knowledge.

# board
BORDER = "#"
UNKNOWN_FIELD = "."
ISLAND = " "
FLAGGED = "F"
MINE = "*"
DETONATED_MINE = "X"
MINES_LEFT = " mine(s) remain."
FLAG_REMOVED_AT = "Flag removed at: "

# file
GET_FILE = "Enter the file to load the board from: "
READ_FILE = "r"

# move
GET_ROW = "Please enter a row: "
GET_COL = "Please enter a column: "
INVAL_NUM = "This number is not valid. Please enter a valid number."
ENTER_R = "Enter 'r' to reveal the space, or"
ENTER_F = "enter 'f' to flag the space: "
REVEAL_SPACE = "r"
FLAG_SPACE = "f"
INVAL_ACTION = "\tThat is not a valid action."
FLAGGED_NO_REVEAL = "\tThis move is flagged! Unflag it to reveal the space!"
ALREADY_REVEALED = "\tThis spot is already revealed."
AV_NO_FLAG = "This field is already revealed. It cannot be flagged."

# game win/loss
GAME_WON = 1
GAME_NOT_OVER = 0
YOU_WON = "\tYou won!"
YOU_LOST = "\tYou detonated a mine, you lost!"


######################################################################
# printBoard()       prints the board with row and column labels,
#                    and spaces the board out so that it looks square
# Input:             board; the rectangular 2d gameboard to print
# Output:            None; prints the board in a pretty way
def printBoard(board):

    # print board code provided to us
    print()
    if len(board[0]) - 2 >= 10:
        print("{:25s}".format(""), end="")
        for i in range(10, len(board[0]) - 1):
            print(str(i//10), end=" ")
        print()

    print("       ", end="")
    for i in range(1, len(board[0]) - 1):
        print(str(i % 10), end=" ")
    print()

    borderRow = "     "
    for col in range(len(board[0])):
        borderRow += board[0][col] + " "

    print(borderRow)

    for row in range(1, len(board) - 1):
        print("{:3d}  ".format(row), end="")
        for col in range(len(board[row])):
            print(str(board[row][col]), end=" ")
        print()

    print(borderRow, "\n")

######################################################################
# populateBoard(): puts unknown fields on the displayBoard
# Parameters:      displayBoard; the current display board
#                  board; the hidden board
# Output:          displayBoard; the displayBoard, now filled
def populateBoard(displayBoard, board):

    # for every spot on the board
    for i in range(len(board)):
        tempRow = board[i]
        for j in range(len(board[i])):
            # replace everything with an unknown field (".")
            if tempRow[j] == ISLAND:
                displayBoard = setCoordinate(displayBoard, i, \
                                             j, UNKNOWN_FIELD)
            elif tempRow[j] == MINE:
                displayBoard = setCoordinate(displayBoard, i, \
                                             j, UNKNOWN_FIELD)
    return displayBoard


######################################################################
# setCoordinate(): sets a coordinate on the board at row, col
# Parameters:      board; the current board
#                  row; the row coordinate
#                  col; the column coordinate
#                  symbol; the symbol to be placed
# Output:          returnBoard; the board with the coordinate now on it
def setCoordinate(board, row, col, symbol):

    # breaks up board for easy setting
    board = breakUpBoard(board)
    # sets symbol at (row, col)
    board[row][col] = symbol
    # repairs the board before return
    return repairBoard(board)

######################################################################
# convertBoard(): rids of the "\n" on each line.
# Parameters:     board; the board the rid \n out of each line
# Output:         newBoard; the board, without the \n's
def convertBoard(board):

    # creates a new board
    newBoard = []
    # traverses the board
    for i in range(len(board)):
        # rids of the \n
        tempBoard = board[i][:len(board[i]) - 1]
        # appends it
        newBoard.append(tempBoard)

    # the new list
    return newBoard
    
######################################################################
# getBoard(): retrives the board from the file the user wants to play
# Parameters: None;
# Output:     board; the board to be stored for the user.
def getBoard():

    board = []

    # gets the file from which to load the board from.
    fileStr = input(GET_FILE)
    # opens the file to read from.
    readFromFile = open(fileStr, READ_FILE)
    # reads the file and sets the board to the file.
    board = readFromFile.readlines()
    # rids of the "\n" in the board
    board = convertBoard(board)
    # closes the board
    readFromFile.close()
    # returns the board
    return board

######################################################################
# getUserCoordinate(): gets the coordinate the user wants to play
# Parameters:          inclusiveRow; the row limit (INCLUSIVE)
#                      inclusiveCol; the column limit (INCLUSIVE)
# Output:              a list, len 2, with the row and column to play
def getUserCoordinate(inclusiveRow, inclusiveCol):

    row = input(GET_ROW)
    # keep in mind THIS ONLY WORKS FOR NUMBERS, FIX THIS
    while int(row) < 1 or int(row) > inclusiveRow:
        print(INVAL_NUM)
        row = input(GET_ROW)

    col = input(GET_COL)
    while int(col) < 1 or int(col) > inclusiveCol:
        print(INVAL_NUM)
        col = input(GET_COL)

    return [int(row), int(col)]


######################################################################
# getMinesLeft(): prints the amount of mines left to flag on the board
# Parameters:     disp; the display board
#                 hidden; the hidden board
# Output:         None; result is printed
def getMinesLeft(disp, hidden):

    minesLeft = 0
    # for every spot on the hidden board...
    for i in range(len(hidden)):
        for j in range(len(hidden[i])):
            # if flag is found...
            if disp[i][j] == FLAGGED:
                # mines left decreases
                minesLeft -= 1
            # if mine is found
            if hidden[i][j] == MINE:
                # the amount of mines left increases
                minesLeft += 1
    # prints mines left
    print(str(minesLeft) + MINES_LEFT)
                

######################################################################
# playMove(): plays the move the user wants to play, reveals islands
# Parameters: disp; the display board
#             hidden; the hidden board to compare disp to
#             coord; the coordinate to play
# Output:     disp; the updated display board
def playMove(disp, hidden, coord):

    # gets initial choice
    choice = ""
    print(ENTER_R)
    choice = input(ENTER_F)
    choice = choice.lower()
    # re-prompts the user to input a valid choice
    while choice != REVEAL_SPACE and choice != FLAG_SPACE:
        print(INVAL_ACTION) # invalid action msg
        print(ENTER_R)
        choice = input(ENTER_F)
        choice = choice.lower()

    # sets coordinate
    onBoard = disp[coord[0]][coord[1]]
    onHiddenBoard = hidden[coord[0]][coord[1]]
    # if the user chose to reveal the space...
    if choice == REVEAL_SPACE:
        # ...check if it's not flagged
        if onBoard != FLAGGED:
            # if the field isn't already revealed, set coordinate
            if onBoard == UNKNOWN_FIELD:
                disp = setCoordinate(disp, coord[0], coord[1], \
                                     onHiddenBoard)
            # if it is already revealed, print already revealed msg
            else:
                print(ALREADY_REVEALED)
        # if it's already flagged, print a cant reveal msg
        else:
            print(FLAGGED_NO_REVEAL)
    # if the user choice to flag the space
    elif choice == FLAG_SPACE:
        # if it's already flagged, remove flag
        if onBoard == FLAGGED:
            print(FLAG_REMOVED_AT + str(coord[0]) + ", " + str(coord[1]))
            disp = setCoordinate(disp, coord[0], coord[1], UNKNOWN_FIELD)
        # if it's already revealed, print can't reavealed msg
        elif onBoard != UNKNOWN_FIELD:
            print(AV_NO_FLAG)
        # if it can be flagged, it will flag it
        elif onBoard == UNKNOWN_FIELD:
            disp = setCoordinate(disp, coord[0], coord[1], FLAGGED)

    # if that place on the hidden board is an island, reveal all
    # adjacent islands. This is where the recursive reveal is.
    if onHiddenBoard == ISLAND:
        # breaks up board for easy setting
        disp = breakUpBoard(disp)
        # reveal islands
        disp = recursiveIslandReveal(getCoordinatesToSwap(disp, hidden, coord), disp, hidden)
        # put board back together
        disp = repairBoard(disp)
        
    return disp


######################################################################
# getTotalMines(): finds the total amount of mines on board
# Parameters:      board; the board to find mines on
# Output:          totalMines; the total amount of mines
def getTotalMines(board):

    totalMines = 0
    # for every spot on the board
    for i in range(len(board)):
        tempRow = board[i]
        for j in range(len(tempRow)):
            # if it's a mine, increases total mines by 1
            if tempRow[j] == MINE:
                totalMines += 1

    return totalMines


######################################################################
# checkForLoss(): checks if the game is still going, lost, or won
# Parameters:     disp; the display board
#                 hidden; the hidden board
#                 mines; the amount of mines
# Output:         1 if won, 0 if game is still going; a list length 2
#                 with the coordinate of where the detonated mine is
def checkForLoss(disp, hidden, mines):

    minesFlagged = 0
    totalFlags = 0
    # for every spot on the board
    for i in range(len(hidden)):
        # temp rows
        tempDisplay = disp[i]
        tempHidden = hidden[i]
        for j in range(len(tempDisplay)):
            # if board is flagged here, total flags + 1
            if tempDisplay[j] == FLAGGED:
                totalFlags += 1
            # if the hidden board has mine here...
            if tempHidden[j] == MINE:
                # ...and the display has a mine here, you lost.
                if tempDisplay[j] == MINE:
                    # returns coordinate to set a detonated mine
                    # symbol on
                    return [i, j]
                # ...and it's flagged, mines flagged + 1
                elif tempDisplay[j] == FLAGGED:
                    minesFlagged += 1

    # the win condition
    if totalFlags == mines and minesFlagged == mines:
        return 1

    # keep going with the game.
    return 0


######################################################################
# findHints(): finds where hints are needed and sets them on the board
# Parameters:  board; the board to find the hints on
# Output:      the board, now with hints on it!
def findHints(board):

    # breaks up the board
    brokenUpBoard = breakUpBoard(board)
    # for every spot on the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            # if the spot is a hint...
            if board[i][j] != BORDER and board[i][j] != MINE:
                # find the hint number
                hint = checkCircleAround(board, i, j)
                # sets that hint number if it's > 0
                if hint > 0:
                    brokenUpBoard[i][j] = hint

    # repairs board before returning
    return repairBoard(brokenUpBoard)


######################################################################
# checkCircleAround(): helper function for findHints, finds hint value
#                      at (row, col)
# Parameters:          board; the board to find hints at
#                      row; the row 
#                      col; the column
# Output:              hint; the hint integer
def checkCircleAround(board, row, col):

    # top row
    rowStart = row - 1
    # bottom row
    rowEnd = row + 1
    # start column of row
    colStart = col - 1
    # end column of row
    colEnd = col + 1

    hint = 0
    # for those three rows
    for i in range(rowStart, rowEnd + 1):
        for j in range(colStart, colEnd + 1):
            # if there's a mine near it, add 1 to mine count
            if board[i][j] == MINE:
                hint += 1

    return hint
    
    
#######################################################################
# breakUpBoard(): breaks up the string board into individual characters
#                 for easier setting of the board
# Parameters:     board; the board to break up
# Output:         newBoard; a broken up board
def breakUpBoard(board):

    newBoard = []
    # for every spot on the board
    for i in range(len(board)):
        # add a row
        newBoard.append([])
        for j in range(len(board[i])):
            # add the spot to the new board
            newBoard[i].append(board[i][j])

    return newBoard


###################################################################
# repairBoard(): repairs the board back into string form
# Parameters:    broken; the broken board
# Output:        newBoard; the repaired board
def repairBoard(broken):

    newBoard = []
    # for every spot on the broken board
    for i in range(len(broken)):
        # add a string to represent a row
        newBoard.append("")
        for j in range(len(broken[i])):
            # adds to the string
            newBoard[i] += str(broken[i][j])

    return newBoard


###################################################################
# endGame():  prints the board, prints win/loss message
# Parameters: winner; the win/loss value
#             board; the board to be printed
# Output:     None
def endGame(winner, board):

    # prints board one last time
    printBoard(board)

    # if you win, print win msg
    if winner == GAME_WON:
        print(YOU_WON)
    # if lost, print lost msg
    else:
        print(YOU_LOST)


###################################################################
# getCoordinatesToSwap(): Finds the coordinates of the islands and
#                         some hints to reveal
# Parameters:             disp; the BROKEN UP display board
#                         board; the hidden board to compare it to
#                         coord; a list, len 2, of coordinate value
# Output:                 swap; a list full of coordinate lists (len
#                         2) for values to reveal
def getCoordinatesToSwap(disp, board, coord):

    swap = []

    # checks start column and left of it
    doLoop = True # loop
    # the checks are done by, from coordinate to hint/border,
    # then coordinate to hint/border
    bottomDone = False # if the bottom of the vertical check is done
    topDone = False # if the top of the vertical check is done
    row = coord[0] # the row
    tempRow = coord[0] # the row, for resetting
    col = coord[1] # the column -1
    nextCheck = False # if there is another column to check
    nextCheckRow = 0 # the row to start checking on the next column
    # loop until no more islands found to reveal
    while doLoop == True:
        # the point on the hidden board
        place = board[row][col]
        # if the point is not a border and it's not column 0
        if place != BORDER and col != 0:
            # if the point is not an island
            if place != ISLAND:
                # add that coordinate
                swap.append([int(row), int(col)])
                # if both top and bottom checks are done...
                if topDone == True and bottomDone == True:
                    # ...and there's no more columns to set...
                    if nextCheck == False:
                        # end the loop. we are done.
                        doLoop = False
                    # ...and there is another column to set
                    else:
                        # go a column left
                        col -= 1
                        # set top and bottom done
                        topDone = False
                        bottomDone = False
                        # the row to start checking on
                        row = nextCheckRow
                        # reset next check flag
                        nextCheck = False
                # if either the top and/or bottom checks aren't done
                else:
                    # if the bottom isn't done being checked
                    if bottomDone != True:
                        # bottom check is done, set row back to start
                        bottomDone = True
                        row = tempRow
                    # if the top is done
                    else:
                        # then the top is done.
                        topDone = True
            # if it is an island
            else:
                # add that coordinate
                swap.append([int(row), int(col)])
                # if there is no next check
                if nextCheck == False:
                    # check for a next check, if the column next to it
                    # is an island, there is a next check
                    if board[row][col - 1] == ISLAND:
                        nextCheck = True
                        nextCheckRow = row
                # if the bottom is done...
                if bottomDone == True:
                    # ...go up a row
                    row -= 1
                else:
                    # ...go down a row
                    row += 1
        # if it is a border or the column is 0
        else:
            # check if bottom is not done
            if bottomDone == False:
                # if it's not, set the bottom to done
                bottomDone = True
                row = tempRow
            # if the column is zero, terminate the loop
            elif col == 0:
                doLoop = False
            # if the bottom is done
            else:
                # reset
                topDone = True
                row = nextCheckRow
                nextCheck = False
                topDone = False
                bottomDone = False
                col -= 1
            

    # finds all spots to the right, NOT INCLUDING START COLUMN
    col = coord[1] + 1
    row = coord[0]
    if board[row][col] != BORDER:
        doLoop = True
        bottomDone = False
        topDone = False
        tempRow = coord[0]
        nextCheck = False
        nextCheckRow = 0
        while doLoop == True:
            place = board[row][col]
            if place != BORDER:
                if place != ISLAND:
                    swap.append([int(row), int(col)])
                    if topDone == True and bottomDone == True:
                        if nextCheck == False:
                            doLoop = False
                        else:
                            col += 1
                            topDone = False
                            bottomDone = False
                            row = nextCheckRow
                            nextCheck = False
                    else:
                        if bottomDone != True:
                            bottomDone = True
                            row = tempRow
                        else:
                            topDone = True
                else:
                    swap.append([int(row), int(col)])
                    if nextCheck == False:
                        if board[row][col + 1] == ISLAND:
                            nextCheck = True
                            nextCheckRow = row
                    if bottomDone == True:
                        row -= 1
                    else:
                        row += 1
            else:
                if bottomDone == False:
                    bottomDone = True
                    row = tempRow
                else:
                    topDone = True
                    row = nextCheckRow
                    nextCheck = False
                    topDone = False
                    bottomDone = False
                    col += 1
        
                        
    return swap
    

##################################################################
# updateHintBorders(): updates the borders that haven't been revealed
# Parameters:          disp; the display board
#                      hidden; the hidden board
# Output:              the board, with updated hint reveals
def updateHintBorders(disp, hidden):

    # for every spot on the board, excluding borders
    for i in range(1, len(disp) - 1):
        for j in range(1, len(disp[i]) - 1):
            # if it's an island on the display board
            if disp[i][j] == ISLAND:
                # check 3x3, with (i, j) being middle of 3x3
                topLeft = i - 1
                for row in range(topLeft, topLeft + 3):
                    for col in range(j-1, j+2):
                        check = hidden[row][col]
                        # if it's not an island or a border,
                        # set to appropriate hint.
                        if check != ISLAND and check != BORDER:
                            disp[row][col] = str(check)

    # repairs board before returning
    return repairBoard(disp)


############################################################################
# recursiveIslandReveal(): A recursive function the reveals all islands
# Parameters:              coordinates; a list full of coordinates to reveal
#                          disp; the display board, BROKEN UP
#                          hidden; the hidden board
# Output:                  the board, now updated with revealed islands
def recursiveIslandReveal(coordinates, disp, hidden):

    # if there are no more coordinates to set, return the current board
    if len(coordinates) == 0:
        return disp
    coord = coordinates[0]
    # sets coordinate
    disp[coord[0]][coord[1]] = str(hidden[coord[0]][coord[1]])
    # returns with one less coordinate to set
    return recursiveIslandReveal(coordinates[1:], disp, hidden)

        
def main():

    # the board.
    board = getBoard()
    # the display board, deep copy of board
    displayBoard = list(board)
    # makes the display board look nice :)
    displayBoard = populateBoard(displayBoard, board)
    # finds total mines on the board
    totalMines = getTotalMines(board)
    # finds the hints for the board
    board = findHints(board)
    # temp variables
    boardWidth = len(displayBoard) - 2
    boardHeight = len(displayBoard[0]) - 2
    winner = ""
    gameIsOver = False
    # game loop
    while gameIsOver == False:
        # prints the board
        printBoard(displayBoard)
        # prints mines left
        getMinesLeft(displayBoard, board)
        # gets the user's coordinate to play
        coord = getUserCoordinate(boardWidth, boardHeight)
        # updates the display board
        # call for island recursion located at end of playMove()
        displayBoard = playMove(displayBoard, board, coord)
        # shows hints on board where needed
        displayBoard = updateHintBorders(breakUpBoard(displayBoard), board)
        # checks if the game is over, if so, it ends the game.
        winner = checkForLoss(displayBoard, board, totalMines)
        # checks if the game should still go on or not (ends the game)
        if winner != GAME_NOT_OVER:
            # sets game status to over
            gameIsOver = True
            # if the winner lost...
            if winner != GAME_WON:
                # ...show the detonated bomb on the screen
                displayBoard = setCoordinate(displayBoard, winner[0], \
                                             winner[1], DETONATED_MINE)
    # ends the game
    endGame(winner, displayBoard)


main()
