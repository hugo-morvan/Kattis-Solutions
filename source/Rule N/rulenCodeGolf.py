# #239
# n,l,r=map(int,input().split())
# s="0"*(r+1)+input()+"0"*(r+1)
# p=["111","110","101","100","011","010","001","000"]
# for i in range(r+1):
#  s="".join([bin(n)[2:].zfill(8)[p.index(s[j-1:j+2])] for j in range(1,len(s)-1)])
#  print(s[r-i:i-r])

 #228
# n,l,r=map(int,input().split())
# a="0"*(r+1)
# s=a+input()+a
# for i in range(r+1):s="".join([bin(n)[2:].zfill(8)[["111","110","101","100","011","010","001","000"].index(s[j-1:j+2])] for j in range(1,len(s)-1)]);print((s)[r-i:i-r])

#224
n,_,r=map(int,input().split())
a="0"*(r+1)
s=a+input()+a
for i in range(r+1):s="".join([bin(n)[2:].zfill(8)[["111","110","101","100","011","010","001","000"].index(s[j:j+3])] for j in range(len(s)-2)]);print(s[r-i:i-r])