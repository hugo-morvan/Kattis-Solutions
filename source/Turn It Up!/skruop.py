# v = 7
# n = int(input())
# for _ in [0]*n:
#     if len(input())>8:
#         v = max(v-1,0)
#     else:
#         v = min(v+1,10)
# print(v)

#87
# v=7
# for _ in [0]*int(input()):v=max(v-1,0)if len(input())>8 else min(v+1,10)
# print(v)

#83
v=7
exec("v=max(v-1,0)if len(input())>8 else min(v+1,10);"*int(input()))
print(v)

#
v=7
exec("v=min(10,max(0,v+(1-2*(len(input())>8))));"*int(input()))
print(v)

v=7
exec("v=min(10,max(0,v+(1-2*(len(input())>8))));"*int(input()))
print(v)