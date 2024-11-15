n,m = map(int,input().split())
buf=''
count = 0
for i in range(n):
    s = input()
    for j in range(m):
        if s[j]=='*':
            buf+=f'\n{i+1} {j+1}'
            count+=1
print(count,buf)
