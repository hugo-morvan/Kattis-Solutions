n = int(input())

days = set() # set to keep track of days when free food is available

for i in range(n):
    start, end = map(int, input().split())
    for j in range(start, end+1):
        days.add(j)

print(len(days)) # number of unique days when free food is available
