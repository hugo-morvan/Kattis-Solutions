l, r = map(int, input().split())

if l == 0 and r == 0:
    print("Not a moose")
else:
    if l == r:
        print("Even", l+r)
    else:
        print("Odd", max(l,r)*2)

