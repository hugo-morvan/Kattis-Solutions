n,x = map(int,input().split())
t=sorted(map(int,input().split()))
if n==1:print('1')
elif t[-1]+t[-2]<=x:print(n)
else:
 for i,c in enumerate(t):
  if c+t[i+1]>x:
   print(i+1)
   break