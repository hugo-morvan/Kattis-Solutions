n, p, s = map(int, input().split())

for i in range(s):
    choices = set(map(int, input().split()[1:]))
    if p in choices:
        print("KEEP")
    else:
        print("REMOVE")
