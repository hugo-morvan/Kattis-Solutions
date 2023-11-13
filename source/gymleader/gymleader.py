n,k,m=map(int,input().split())

#create a 2D array of size n x n
al=[[0 for i in range(n+1)] for j in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    al[a-1][b-1]=1
    al[b-1][a-1]=1
#print("initial")
#print(al)
def calcSum():
    for i in range(n):
        tot=al[i][n]
        al[i][n]=sum(al[i])-tot
#print("sum")
calcSum()

#total column is al[i][n], n is the last column

#clear the rows that have total column less than or equal to 1
for i in range(100000):
    for j in range(n):
        if al[j][n]<=1:
            #clear the row and the column
            for k in range(n+1):
                al[j][k]=0
            for k in range(n):
                al[k][j]=0
    #print("iteration",i)
    calcSum()
    #print(al)

print(['NO','YES'][al[k][n]==0])


