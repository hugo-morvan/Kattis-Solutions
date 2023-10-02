# s,t=input(),''
# while s:
#  if s[0]!=t:
#   t=s[0]
#   print(t,end='')
#  s=s[1:]

s,a=input(),' '
while s:
 if s[0]!=a[-1]:a+=s[0]
 _,*s=s
print(a[1:])
