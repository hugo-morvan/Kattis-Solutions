n,m=int(input()),int(input())
r = m%n
for i in range(r):
    print((m//n+1)*'*')
for i in range(n-r):
    print((m//n)*'*')