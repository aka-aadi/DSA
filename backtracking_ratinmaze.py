def solve_maze(maze):
    n = len(maze)
    sol = [[0]*n for _ in range(n)]
    def solve(x, y):
        if x == n-1 and y == n-1:
            sol[x][y] = 1
            return True
        if 0 <= x < n and 0 <= y < n and maze[x][y]:
            sol[x][y] = 1
            jumps = maze[x][y]
            for j in range(1, jumps+1):
                if y+j < n and solve(x, y+j) or x+j < n and solve(x+j, y):
                    return True
            sol[x][y] = 0
        return False
    return sol if solve(0, 0) else [[-1]]

for _ in range(int(input())):
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]
    sol = solve_maze(maze)
    if sol[0][0] == -1:
        print(-1)
    else:
        for row in sol:
            print(*row)