s=input()
t,l=0,s.count('<')
for i in [0]*len(s):
 if s[i]=='<':l-=1
 if s[i]=='>':t+=l
print(t)

#convert the above code to python