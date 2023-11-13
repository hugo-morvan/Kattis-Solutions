n, q = map(int, input().split())
locations = list(map(int, input().split()))

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        locations[query[1]-1] = query[2]
    else:
        print(abs(locations[query[1]-1] - locations[query[2]-1]))
