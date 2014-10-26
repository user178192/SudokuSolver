import sys
import csv
import message
__author__ = 'star'

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.

    # Get empty position for all board
    def __init__(self):
        self.result = [[0 for col in xrange(9)] for row in xrange(9)]

    def get_empty(self, board):
        for i in xrange(81):
            if board[i / 9][i % 9] == 0:
                return i / 9, i % 9
        return -1, -1

    # check the board is vaild or not
    def check_board(self, board):
        if len(board) != 9:
            return False
        else:
            for row in board:
                if len(row) != 9:
                    return False
                for num in row:
                    if num < 0 or num > 9:
                        return False
        return True

    # Determine every solution is valid or invalid
    def is_valid(self, board, element, row, col):
        # Same value in the same column or row ?
        for i in xrange(9):
            if (i != col and board[row][i] == element) or (i != row and board[i][col] == element):
                return False

        # Same value in the 3 * 3 block it belong to ?
        for i in xrange(row / 3 * 3, row / 3 * 3 + 3):
            for j in xrange(col / 3 * 3, col / 3 * 3 + 3):
                if i != row and j != col and board[i][j] == element:
                    return False
        return True

    # Using Depth First Search to fill the numbers 1~9
    def solve_sudoku(self, board):
        i, j = self.get_empty(board)
        # Fill down success
        if i == -1 and j == -1:
            return True
        # Using depth first search to fill the numbers 1 ~ 9
        for k in xrange(1, 10):
            board[i][j] = k
            if self.is_valid(board, k, i, j) and self.solve_sudoku(board):
                return True
            board[i][j] = 0
        return False


def get_result(result):
    tester = Solution()
    if tester.check_board(result) is False:
        return message.invaild_msg, result

    if tester.solve_sudoku(result):
        return message.suc_msg, result
    else:
        return message.nosol_msg, result

if __name__ == "__main__":
    result = []
    if len(sys.argv) < 3:
        print message.usage_msg
        sys.exit()

    with open(sys.argv[1], 'r') as fin:
        for line in fin:
            result.append(map(int, line.split(',')))

    tester = Solution()
    if tester.check_board(result) is False:
        print message.invaild_msg
        sys.exit()

    with open(sys.argv[2], 'w') as fout:
        if tester.solve_sudoku(result):
            csv_file = csv.writer(fout)
            csv_file.writerows(result)
            print message.suc_msg, sys.argv[2]
        else:
            print message.nosol_msg
            sys.exit()