
def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]

    def is_safe(row, col):
        # Check column above
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1

                if backtrack(row + 1):
                    return True

                board[row][col] = 0

        return False

    # Place the first queen at (0, 0)
    board[0][0] = 1

    if backtrack(1):
        print("\nFinal N-Queens Matrix:")
        for row in board:
            print(row)
    else:
        print("No solution exists.")

n = int(input("Enter the value of N: "))

if n >= 1:
    solve_nqueens(n)
else:
    print("Enter a positive number.")
