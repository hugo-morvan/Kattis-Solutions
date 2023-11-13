# s=input()
# nums=input()
# ids=""
# for i in range(len(nums)//3):
#     ids+=s[int(nums[i*3:i*3+3])-1]
# print(ids)

#80
# s,n=input(),input()
# for i in range(0,len(n),3):print(s[int(n[i:i+3])-1],end="")

# s,n=input(),input()
# print(*[s[int(n[i:i+3])-1]for i in range(0,len(n),3)],sep="")

#67
# s,n=input(),input()
# while(n):print(s[int(n[:3])-1],end="");n=n[3:]

s,n=input(),input()
while(n):print(s[int(n[:3])-1],end="");n=n[3:]
