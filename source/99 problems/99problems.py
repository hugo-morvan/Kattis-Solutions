n=l=h=int(input())
while l%100!=99:l-=1
while h%100!=99:h+=1
print(l if (n-l<h-n)*l>0 else h)

