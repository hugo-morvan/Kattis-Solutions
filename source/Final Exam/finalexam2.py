i=input
n=int(i())-1
a=i()
for _ in [0]*n:
 b=i()
 n-=a!=b
 a=b
print(n)