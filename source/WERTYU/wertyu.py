k=['`1234567890-=','QWERTYUIOP[]\\','ASDFGHJKL;\'','ZXCVBNM,./']
while(1):
 try:
  l=input()
 except EOFError:
  break
 for i in range(len(l)):
  for j in range(len(k)):
   if l[i] in k[j]:
    l=l[:i]+k[j][k[j].index(l[i])-1]+l[i+1:]
 print(l)
