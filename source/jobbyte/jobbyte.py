n=int(input())
a=[*map(int,input().split())]
length = len(a)
seen = [False]*length
def cycle_length(a, idx):
    if seen[idx]: return 0
    seen[idx] = True
    return 1 + cycle_length(a, a[idx]-1)

print(max(cycle_length(a, i) for i in range(length))-1)

