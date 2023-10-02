n=int(input())
for i in range(n):
    a,b,c=input(),input(),""
    for j in range(len(a)):
        c+="." if a[j]==b[j] else "*"
    print(a)
    print(b)
    print(c)
    print()

