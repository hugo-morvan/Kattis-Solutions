list = [sum([eval(i) for i in input().split()]) for _ in range(5)]
print(list.index(int(max(list)))+1, max(list))