m = int(input())
n = int(input())
a = 0
b = 0
for i in range(n):
    s = input()
    a += s.count(".")
    b += len(s)
print(a/b)