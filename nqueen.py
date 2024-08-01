def solveNQueens(n):
    def isSafe(board, row, col):
        # Check column and diagonals
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
   
    def solve(board, row):
        if row == n:
            solutions.append(board[:])
            return
       
        for col in range(n):
            if isSafe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                # Backtrack
                board[row] = -1
   
    solutions = []
    board = [-1] * n
    solve(board, 0)
   
    return solutions

def printSolutions(solutions):
    result = []
    for sol in solutions:
        formatted_solution = f"[{' '.join(str(col + 1) for col in sol)} ]"
        result.append(formatted_solution)
    print(' '.join(result))

# Input and Output
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip()
    n = int(data)
   
    solutions = solveNQueens(n)
    if solutions:
        printSolutions(solutions)
    else:
        print("-1")
