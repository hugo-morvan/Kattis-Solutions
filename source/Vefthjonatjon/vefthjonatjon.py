n = int(input())
row = [0]*n
for i in range(n):
    row[i] = list(input().split())
ans = 9999999999
for cols in range(len(row[0])):
    sum_col = 0
    for r in range(n):
        if row[r][cols]=='J':
            sum_col += 1
    ans = min(sum_col, ans)
print(ans)