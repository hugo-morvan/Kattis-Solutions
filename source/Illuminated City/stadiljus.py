n = int(input())
x = int(input())
y = int(input())
L = list(map(int, input().split()))

costs = map(lambda l: l*x, L)
sorted_costs = sorted(costs)
selection = []
while len(sorted_costs)>0:
    selection.append(sorted_costs.pop(0))
    if len(selection)>0:
        if sum(selection)/len(selection) >= y:
            break

    
print(len(selection))