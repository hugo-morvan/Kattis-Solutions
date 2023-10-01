import math

n, w, h = map(int, input().split())
diagonal = math.sqrt(w**2 + h**2)

for i in range(n):
    length = int(input())
    if length <= diagonal:
        print("DA")
    else:
        print("NE")
