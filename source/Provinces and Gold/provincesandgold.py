# #280
# w=['Province','Duchy','Estate','Gold','Silver','Copper'];p=print
# b=[int(i) for i in input.split()]
# c=b[0]*3+b[1]*2+b[2]*1
# if c>=8:p(w[0],'or',w[3])
# elif c>=6:p(w[1],'or',w[3])
# elif c>=5:p(w[1],'or',w[4])
# elif c>=3:p(w[2],'or',w[3])
# elif c>=2:p(w[2],'or',w[4])
# else:p(w[5])

# w,d=['','Estate or ','Duchy or ','Province or '],['Copper','Silver','Gold']
# b=sum([int(i)*j for i,j in zip(input().split(),[3,2,1])])
# print(w[(b+1)//3 if b<9 else 2],d[b//3 if b<8 else 2], sep='')

# #195
# l=['','Copper','Estate or ','Silver','Duchy or ','Gold','Province or ']
# b=sum([int(i)*j for i,j in zip(input().split(),[3,2,1])])
# print(l[((b+1)//3)*2 if b<11 else 6]+l[(b//3)*2+1 if b<9 else 5])

#181
# b=sum([int(i)*j for i,j in zip(input().split(),[3,2,1])])
# print(['','Estate or ','Duchy or ','Province or '][(b+1)//3 if b<8 else 3]+['Copper','Silver','Gold'][b//3 if b<9 else 2])

# b=sum([int(i)*j for i,j in zip(input().split(),[3,2,1])])
# print(['','Estate or ','Duchy or ','Province or '][(b+1)//3 if b<8 else 3]+['Copper','Silver','Gold'][b//3 if b<9 else 2])

#180
a,b,c=input().split();i=int
b=i(a)*3+i(b)*2+i(c)
print(['','Estate or ','Duchy or ','Province or '][(b+1)//3 if b<8 else 3]+['Copper','Silver','Gold'][b//3 if b<9 else 2])


