# a = input().split("|")
# b = input().split("|")
# ans=[]
# for i in range(len(a)):
#     ans.append(a[i])
#     ans.append(b[i])
#     ans.append(" ")
# print(*ans, sep="")

# a,b=input().split("|"),input().split("|")
# print(*[a[i]+b[i]+" " for i in range(len(a))],sep="")

print(*[a+b+" " for a,b in zip(input().split("|"),input().split("|"))],sep="")


