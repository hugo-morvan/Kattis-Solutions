n=int(input())
#make a 2D array of size n*n
table=[[0 for i in range(n)] for j in range(n)]
#read in the table
for i in range(n):
    table[i]=list(map(int,input().split()))
solution=[]
for i in range(n):
    for j in range(n):
        if table[i][j]>0:
            solution+=[(i,j)]
print(len(solution))
for i in solution:
    print(i[0]+1,i[1]+1, table[i[0]][i[1]])
