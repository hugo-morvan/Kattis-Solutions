g,n=map(int,input().split())
t=[[*map(int,input().split())]for _ in[0]*n]
t.sort(key=lambda x:x[1])
p,c=1,t[0][1]
for y in t:
 if y[0]>=c:c=y[1];p+=1
print(['YES','NO'][p<g])