n,s=input().split()
p=0
a={'A':11,'K':4,'Q':3,'J':20,'T':10,'9':14,'8':0,'7':0}
b={'A':11,'K':4,'Q':3,'J':2,'T':10,'9':0,'8':0,'7':0}
for _ in range(int(n)*4):
    h=input()
    if h[1]==s:p+=a[h[0]]
    else:p+=b[h[0]]
print(p)
#
##180
#n,s=input().split()
#a,b=[11,4,3,2,10,0,0,0],[20,14]
#print(sum([b['J9'.index(c[0])]if c[1]==s and c[0]in'J9'else a['AKQJT987'.index(c[0])]for _ in[0]*int(n)*4 for c in[input()]]))
#
##180
#n,s=input().split()
#a,z=[20,14,2,0,11,4,3,10,0,0],'J9AKQT87'
#print(sum([a[z.index(c[0])]if c[1]==s and c[0] in'J9'else a[z.index(c[0])+2]for _ in[0]*int(n)*4 for c in[input()]]))
#
##181
#h,u,(g,o)=[20,14,2,0,11,4,3,10,0,0],'J9AKQT87',input().split()
#print(sum([h[u.index(c[0])]if c[1]==o and c[0] in'J9'else h[u.index(c[0])+2]for _ in[0]*int(g)*4 for c in[input()]]))
#
##182
#n,s=input().split()
#a,z=[20,14,2,0,11,4,3,10,0,0],'J9AKQT87'
#print(sum((c[1]==s)*a[z.index(c[0])]+(c[1]!=s)*a[z.index(c[0])+2]for _ in[0]*int(n)*4 for c in[input()]))
#
#156
#n,s=input().split()
#a,z=[11,4,3,10,14,0,0,2,0,20,14],'AKQT987J'
#print(sum(a[z.index(c[0])+(c[1]==s and c[0]in'J9')*2]for _ in[0]*int(n)*4 for c in[input()]))

#152
#n,s=input().split()
#a,z=[11,4,3,10,14,0,0,20,2],'AKQT987J'
#print(sum(a[z.index(c[0])+(c[1]!=s and c[0]in'J9')]for _ in[0]*int(n)*4 for c in[input()]))
#
##152
#h,u,(g,o)=[11,4,3,10,14,0,0,20,2],'AKQT987J',input.split()
#print(sum(h[u.index(c[0])+(c[1]!=o and c[0]in'J9')]for _ in[0]*int(g)*4 for c in[input()]))
#
##143
#n,s=input().split()
#print(sum([11,4,3,10,14,0,0,20,2]['AKQT987J'.index(c[0])+(c[1]!=s and c[0]in'J9')]for _ in[0]*int(n)*4 for c in[input()]))

#142
i=input
n,s=i().split
print(sum([11,4,3,10,14,0,0,20,2]['AKQT987J'.index(c[0])+(c[1]!=s and c[0]in'J9')]for _ in[0]*int(n)*4 for c in[i()]))
