"""N Queens Problem - Matthew Laws
"""

def print_one_row(position_of_queen, columns): #print one row repacing 0's with "." and displays "Q" for queens.
    for c in range(0, columns):
        if c == position_of_queen:
            print ("Q" , end = " ")
        else:
            print("." , end = " ")
    print(" ")
    
    
def print_all_rows(rows): #prints entire board.
    columns = len(rows)
    for queen_position in rows:
        print_one_row(queen_position, columns)
        
        
def is_column_valid(board, newColumn): #checking column validity
    for column in range (newColumn):
        if board [column]==board [newColumn]:
            return False
    return True


def is_diagonal_valid(board, newColumn): #checking diagonal validity
    for column in range (newColumn):
        if abs(column-newColumn)==abs(board[column]-board[newColumn]): #absolute(abs) values required to run functions. 
            return False
    return True


def is_board_valid(board, newColumn): #checking valid placement
    return is_column_valid(board, newColumn) and is_diagonal_valid(board, newColumn)


def solve_queens_problem(size) : #generates the board that is passed into the solve function.
    board = [-1]*size #starts with all queens off the board at position -1. Avoids conflicts with is_board_valid and allows solve to run through iterations/backtrack.
    start = 0 #start same as size in solve function, start used to denote start at column 0
    return solve(board,start,size)


def solve(board, column, size):
    if column == size:
        #problem solved / base case
        print_all_rows(board)
        more = input("\nMore? (y/n) ")
        if more == "y" or more == "Y":
            return False
        else:
            return True
        
    else:
        for rowIndex in range (size):
            board[column] = rowIndex
            if is_board_valid(board, column):
                queen_placed = solve(board, column + 1, size) #moving to next column
                if queen_placed: #statement required to halt programe is response to "More?" != "y/Y"
                    
                    return True 
        
        return False
    
    
size = int(input("What size board would you like? ")) #prevents the need for refactoring to different board sizes
solution = solve_queens_problem(size)
print ("Finished") #will print "Finished" when there are no more solutions or input != "y/Y" to "More?"





"""
def is_row_valid(board): #not needed for program however is a placeholder for row validation if needed.
    
    for row in range (len(board)):
        if board[column] < 0 or board[column] >= len(board):
            return False
    
    return True #for this program always returns true at this point because queens can never be placed on the same row, except for their starting position at -1 which is off the board
"""