n = int(input())
kpw=[0,0,0]
for i in range(n):
    w = input()
    if w=='keys':kpw[0]=1
    if w=='phone':kpw[1]=1
    if w=='wallet':kpw[2]=1
if sum(kpw)==3:print('ready')
else:
    p=['keys','phone','wallet']
    for i in range(3):
        if not kpw[i]:print(p[i])