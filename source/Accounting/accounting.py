n,q=map(int,input().split())
d,v="0",{}
for _ in [0]*q:
 i=input()
 if i[0]=="S":_,a,b=i.split();v[a]=b
 elif i[0]=="P":print(v.get(i.split()[1], d))
 else:v.clear();d=i.split()[1]