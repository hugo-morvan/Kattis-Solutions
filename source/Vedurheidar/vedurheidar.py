w = int(input())
n = int(input())
for i in range(n):
    road, lim = input().split()
    if int(lim)<w:
        print(road, "lokud")
    else:
        print(road, "opin")