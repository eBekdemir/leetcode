# URL: https://leetcode.com/problems/valid-sudoku/                        
# TITLE: Valid Sudoku                            
# DIFFICULTY: Medium                                
# ------------------------------------------------------
class Solution(object):
    def row_valid(self, row):
        x = []
        for element in row:
            if element in x and element != '.': return False
            x.append(element)
        return True

    def isValidSudoku(self, board):

        for row in board:
            if not self.row_valid(row): return False
        transpose = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
        for column_to_row in transpose:
            if not self.row_valid(column_to_row): return False

        subbox_elements = []
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[row+i][column+j])
                subbox_elements.append(box)

        for box in subbox_elements:
            if not self.row_valid(box): return False
        
        return True

# ------------------------------------------------------
class Solution:
    def isValidSudoku(self, board):
        for ind, elm in enumerate(board):
            if elm.count('.') + len(set(elm)) != 10: return False
            col = [board[i][ind] for i in range(9)]
            if col.count('.') + len(set(col)) != 10: return False
        for rw in range(0,9,3):
            for colnum in range(0,9,3):
                sqr = []
                for cl in range(3):
                    sqr += board[cl+colnum][rw:rw+3] 
                if sqr.count('.') + len(set(sqr)) != 10: return False
        return True
