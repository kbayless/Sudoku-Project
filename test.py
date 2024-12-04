from sudoku_generator import *

# s1 = SudokuGenerator(9,0)
# s1.fill_values()
# s1.print_board()
# test = s1.board[1][1]
# print(test)
# print(s1.box_length)
# print(s1.valid_in_box(6,6,2))


#is sometimes able to generate a board, sometimes will "stall out?" if you retry enough itll work
#stalling occurs somewhere in fill_remaining function (line 232 of sudoku_generator.py)
#my guess is that it is something to do with the is_valid function (line 164)
#when it does manage to generate a board, it is NOT valid (check this by looking at each 3x3 set)
solved_board, board = generate_sudoku(9,30)
for i in solved_board:
    print(i)
print("test") #this doesn't print when it gets stuck