a, b = map(int, input().split())
for i in range(a):
    b -= int(input())

print(["Neibb","Jebb"][b >= 0])