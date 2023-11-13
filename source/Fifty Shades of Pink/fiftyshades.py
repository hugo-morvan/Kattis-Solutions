n = int(input())
count = 0
for i in range(n):
    color = input().lower()
    if 'pink' in color or 'rose' in color:
        count += 1
if count == 0:
    print('I must watch Star Wars with my daughter')
else:
    print(count)
