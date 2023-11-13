r,c = map(int,input().split())
grid = [['.' for i in range(c)] for j in range(r)]
zero,one,two,three,four = 0,0,0,0,0
for i in range(r):
    line = input()
    for j in range(c):
        grid[i][j] = line[j]
#use a 2*2 convolution to find the number of 'X' in the grid
for i in range(r-1):
    for j in range(c-1):
        window=grid[i][j]+grid[i][j+1]+grid[i+1][j]+grid[i+1][j+1]
        
        if '#' in window: pass
        else:
            count = window.count('X')
            if count == 0: zero+=1
            elif count == 1: one+=1
            elif count == 2: two+=1
            elif count == 3: three+=1
            elif count == 4: four+=1
print(zero)
print(one)
print(two)
print(three)
print(four)

