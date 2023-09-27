s,x=input(),''
P=K=H=T=13
while s:
    c=s[0:3]
    if c in x:print('GRESKA');exit()
    if c[0]=='P':P-=1
    elif c[0]=='K':K-=1
    elif c[0]=='H':H-=1
    else:T-=1
    x+=c
    s=s[3:]
print(P,K,H,T)


