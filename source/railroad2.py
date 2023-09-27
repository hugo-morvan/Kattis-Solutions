# x,y=map(int,input().split())
# print("possible" if y%2==0 else "impossible")

# _,y=input().split()
# print("im" if int(y)%2==1 else "",end="possible")


print("im"*(int(input()[1:])%2)+"possible")