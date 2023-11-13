# n,m=input().split()
# for i in range(100):
#  if n==m:print(i+1);exit()
#  c=''
#  for j in range(10):
#   a=n.count(str(j))
#   c+=str(a)+str(j) if a>0 else ''
#  n=c
# print("Does not appear")

# n,m=input().split()
# r,s,p=range,str,print
# for i in r(100):
#  if n==m:p(i+1);exit()
#  c=''
#  for j in r(10):a=n.count(s(j));c+=s(a)+s(j) if a>0 else ''
#  n=c
# p("Does not appear")

# n,m=input().split()
# s,i=str,0
# while(i<100):
#  if n==m:print(i+1);exit()
#  c=''
#  for j in range(10):a=n.count(s(j));c+=s(a)+s(j) if a>0 else ''
#  n=c;i+=1
# print("Does not appear")


#173
# n,m=input().split()
# s,i=str,0
# while(n!=m):
#  if i==100:print("Does not appear");exit()
#  n=''.join([s(n.count(s(j)))+s(j) for j in range(10) if s(j)in n]);i+=1
# # print(i+1)

# n,m=input().split()
# s,i=str,1
# while n!=m:
#  if i==100:print("Does not appear");exit()
#  n=''.join([s(n.count(s(j)))+s(j) for j in range(10) if s(j)in n]);i+=1
# print(i)

# n,m=input().split()
# i=1
# while n!=m:
#  if i==100:print("Does not appear");exit()
#  n=''.join([str(n.count(s(j)))+str(j) for j in range(10) if str(j)in n]);i+=1
# print(i)


n,m=input().split()
i=1
while(n!=m)*(i<100):
 n=''.join([str(n.count(str(j)))+str(j) for j in range(10) if str(j)in n]);i+=1
print([i,"Does not appear"][i==100])

