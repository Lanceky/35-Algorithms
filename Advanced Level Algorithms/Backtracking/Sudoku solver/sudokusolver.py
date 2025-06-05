def solve_sudoku(board):
    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if is_valid(i, j, num):
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = '.'
                    return False
        return True

    def is_valid(row, col, num):
        for x in range(9):
            if (board[row][x] == num or
                    board[x][col] == num or
                    board[3 * (row // 3) + x // 3][3 * (col // 3) + x % 3] == num):
                return False
        return True

    backtrack()