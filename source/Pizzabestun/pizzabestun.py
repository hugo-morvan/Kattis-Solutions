# n=int(input())
# list=[]
# for i in range(n):
#     name,price=input().split()
#     list.append(int(price))
# list.sort()
# price=0
# for i in range(n//2+(n%2)):
#     price+=list[-1-i*2]

# print(price)

# Version 2
# n,l=int(input()),[]
# list=[l.append(int(input().split()[1])) for i in range(n)]
# l.sort()
# print(sum(l[::-2]))

# Version 3
n=int(input())
l=[int(input().split()[1]) for i in n*[0]]
l.sort()
print(sum(l[::-2]))

# Version 4
n=int(input())
l=[int(input().split()[1]) for i in n*[0]]
l.sort()
print(sum(l[::2]))