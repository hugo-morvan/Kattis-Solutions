n,k,d = map(int, input().split())
c = 0
for i in range(n):
    if int(input())+14 <= k+d: c+=1
print(c)