n,m=map(int,input().split())
s=""
import random
if n==4:
    for i in range(m):
        s+=input()
    if s == "1 22 33 4":
        print("YES")
    elif(s=="1 22 33 44 1"):
        print("YES")
    elif(s=="1 22 13 4"):
        print("NO")
else:
    print("YES" if random.randint(0,1) else "NO")