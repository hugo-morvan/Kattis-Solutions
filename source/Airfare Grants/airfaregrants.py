n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
print(max(0,int(min(l)-max(l)/2)))