n=input
t=int
for i in [0]*t(n()):
 p,r,f=map(t,n().split())
 while p<=f:p*=r;i+=1
 print(i)