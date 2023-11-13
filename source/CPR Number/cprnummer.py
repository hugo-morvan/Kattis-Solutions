# a,b=input().split("-")
# a+=b
# c="4327654321"
# print("1" if sum([int(a[i])*int(c[i]) for i in range(10)])%11==0 else "0")

#100
# a=input().replace("-","")
# print((sum([int(a[i])*int("4327654321"[i]) for i in range(10)])%11==0)*1)

print((sum([int(input().replace("-","")[i])*int("4327654321"[i]) for i in range(10)])%11==0)*1)
