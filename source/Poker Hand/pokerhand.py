r=[c[0]for c in input().split()]
print(max({k: r.count(k) for k in r}.values()))

r=[c[0]for c in input().split()]
print(len([i for i in r if i==max(r)]))