l,x = map(int,input().split())
c=0
d=0
for i in range(x):
    action, num = input().split()
    num = int(num)
    if action=="enter":
        if c+num>l: d += 1
        else: c+=num
    else:
        c -= num
print(d)
