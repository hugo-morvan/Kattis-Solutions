n,m = map(int, input().split())

grid = []
for i in range(n):
    grid.append(list(input()))

for j in range(m):
    for i in range(n):
        if grid[i][j] != '.':
            print(grid[i][j], end='')
            