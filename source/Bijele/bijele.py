# a=[1,1,2,2,2,8]
# b=[int(i) for i in input().split()]
# print(*[i-j for i,j in zip(a,b)])
#71
# print(*[i-j for i,j in zip([1,1,2,2,2,8],[*map(int,input().split())])])
# #78
# a=[*map(int,input().split())];print(*[[1,1,2,2,2,8][n]-a[n]for n in range(6)])

#63
print(*[i-int(j)for i,j in zip([1,1,2,2,2,8],input().split())])

# b=[int(i) for i in input().split()]
# c=[[1,1,2,2,2,8][i]-b[i] for i in range(6)]
# print(*c)
#70
# print(*[[1,1,2,2,2,8][i]-int(input().split()[i]) for i in range(6)])

