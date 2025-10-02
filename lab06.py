# TODO: sorted_cities is given a string of city names separated by commas
# and prints out the names in sorted order.
def sorted_cities(city_names):
    city_list = city_names.split(",")
    city_list.sort()
    return city_list
    

# Debugging function calls.
# The following should print Boston, Chicago Indianapolis
# and San Francisco in that order each city on a new line
print(sorted_cities('San Francisco,Boston,Chicago,Indianapolis'))

# TODO: same_but_different_order is given two lists and returns True
# if lists contain the same elements, possibly in different orders,
# and False otherwise
def same_but_different_order(list1, list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


# Below is our test code. Do not modify it, but you may add your own prints.
assert(same_but_different_order([1, 2, 3], [3, 1, 2]) == True) 
assert(same_but_different_order([1, 1, 1, 2],[1, 2, 1, 1]) == True)
assert(same_but_different_order([1, 2, 3, 1], [1, 2, 3]) == False)
assert(same_but_different_order([1, 1, 2, 3], [1, 3, 2, 2]) == False)

# TODO: Define variables for the characters on the board
x = 'X'
o = 'O'
empty = '_'

# This is an example of how to create a list of only empty spaces
empty_row = [empty, empty, empty]

# TODO: Complete the board so that it has three empty rows
# We have started off with a single empty row
board0 = [[empty, empty, empty]]

# TODO: Complete code that will create the following board
# We have provided code for the first of the three rows
# X _ O, _ X O, X _ _
board1 = [[x, empty, o], [empty, x, o], [x, empty, empty]]

# TODO: Write code to create the following board
# X _ O, _ X O, O _ X
board2 = [[x, empty, o],[empty, x, o],[o, empty, x]]

# TODO: Complete the function has_won that, given a board,
# will return True if and only if the Player X or O passed
# to it has won that board by filling a row, column, or
# diagonal. You may assume all boards are 3 by 3
# and all rows have same length
def has_won(board, player):
    for row in board:
        win = True
        for cell in row:
            if cell != player:
                win = False
                break
        if win:
            return True
    for col in range(3):
        win = True
        for row in range(3):
            if board[row][col] != player:
                win = False
                break
        if win:
            return True
    win = True
    for i in range(3):
        if board[i][i] != player:
            win = False
            break
    if win:
        return True
    win = True
    for i in range(3):
        if board[i][2 - i] != player:
            win = False
            break
    if win:
        return True

    return False
    

# Here is some testing code. You can create new boards
# to test for row and column wins
assert(has_won(board0, x) == False)
assert(has_won(board1, o) == False)
assert(has_won(board2, x) == True)
      
# TODO: For even more challenge if you are interested,
# can you use your board and has_won function
# to complete an implementation for a tic tac toe game?
# Start from an empty board and prompt players for moves
# until a player has won or the board is full