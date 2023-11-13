m,a,b,c = map(int,input().split())
print("possible" if (m-a>1 and m-b>1 and m-c>1) else "impossible")