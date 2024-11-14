w,s = map(int,input().split())
c = (s*(s+1)/2)
for i in range(1,s+1):
    if (w//(i*29260) == i):print(i)