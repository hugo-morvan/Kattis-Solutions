n=int(input())
l=[0]*(n+1)
for i in range(n//2+1):
    a,b=map(int,input().split())
    l[a]+=1
    l[b]+=1

print(*[i for i in range(len(l)) if l[i]==2])

