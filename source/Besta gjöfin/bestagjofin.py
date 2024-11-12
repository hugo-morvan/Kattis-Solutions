n = int(input())
max_name = ''
max_val=0
for i in range(n):
    a,b = input().split()
    if int(b)>max_val:
        max_name = a
        max_val = int(b)
print(max_name)