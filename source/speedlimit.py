n=int(input())
while 1:
    if n == -1:
        break
    else:
        time = 0
        count = 0
        for i in range(n):
            a,b=map(int,input().split())
            count+=a*(b-time)
            time = b
    print(count, "miles")
    n=int(input())
