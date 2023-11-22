d = {'.':20, 'O':10, '\\':25, '/':25, 'A': 35, '^':5, 'v':22}
x,y = map(int,input().split())
sum=0
for i in range(x):
    l = input()
    for c in l:
        sum += d[c]
print(sum)