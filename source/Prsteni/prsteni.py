import math

n = int(input())
radii = list(map(int, input().split()))

for i in range(1, n):
    gcd = math.gcd(radii[0], radii[i])
    ratio = str(radii[0] // gcd) + '/' + str(radii[i] // gcd)
    print(ratio)
