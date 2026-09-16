def solve(board, row, n):

    if row == n:
        return True

    for col in range(n):

        if safe(board, row, col, n):

            board[row][col] = 1

            if solve(board, row + 1, n):
                return True

            board[row][col] = 0   # BACKTRACK

    return False


def safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True
