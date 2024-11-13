#https://open.kattis.com/problems/barcelona

_,bag = input().split()
bags = input().split()
idx = bags.index(bag) + 1
if idx==1:  print("fyrst")
elif idx==2:print('naestfyrst')
else:       print(idx,"fyrst")