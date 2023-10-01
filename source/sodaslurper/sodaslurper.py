e,f,c = input().split()
e=int(e)
f=int(f)
c=int(c)
total = 0
bottles = e+f
while bottles >= c:
    total += bottles//c
    bottles = bottles//c + bottles%c
print(total)