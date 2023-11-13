n, m = map(int, input().split())
perm = list(range(1, n+1))

for _ in range(m):
    a = int(input())
    perm[a-1], perm[a] = perm[a], perm[a-1]

for element in perm:
    print(element)
