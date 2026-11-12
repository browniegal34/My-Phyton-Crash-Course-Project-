def is_safe(board, row, col, n):
    # check column above
    for i in range(row):
        if board[i][col] == 1:
            return False
    # check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def solve(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, row + 1, n):
                return True
            board[row][col] = 0  # backtrack
    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if c else "." for c in row))

try:
    n = int(input("Enter N: "))
except ValueError:
    print("Enter a valid number")
    exit()

board = [[0] * n for _ in range(n)]

if solve(board, 0, n):
    print_board(board)
else:
    print("No solution for N =", n)