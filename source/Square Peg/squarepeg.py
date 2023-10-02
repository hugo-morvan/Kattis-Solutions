import math
l,r = map(int, input().split())
print("fits" if math.sqrt(2*l**2)<=2*r else "nope")