input()
print(['no','yes'][sum(map(int,input().split()))%3==0])