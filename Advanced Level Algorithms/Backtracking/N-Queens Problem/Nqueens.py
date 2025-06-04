def solve_n_queens(n):
    def backtrack(row, cols, diags, anti_diags, board, res):
        if row == n:
            res.append(["".join(row) for row in board])
            return

        for col in range(n):
            d = row - col
            ad = row + col
            if col in cols or d in diags or ad in anti_diags:
                continue

            cols.add(col)
            diags.add(d)
            anti_diags.add(ad)
            board[row][col] = 'Q'

            backtrack(row + 1, cols, diags, anti_diags, board, res)

            board[row][col] = '.'
            cols.remove(col)
            diags.remove(d)
            anti_diags.remove(ad)

    res = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0, set(), set(), set(), board, res)
    return res