i,r=input,range
n=int(i())
while n!=0:
 g=[[0]*500 for _ in r(500)]
 for _ in r(n):
  a,b,c,d=map(int,i().split())
  for j in r(a,c):
   for k in r(b,d):g[j][k]=1
 print(sum(sum(x for x in y) for y in g))
 n=int(i())