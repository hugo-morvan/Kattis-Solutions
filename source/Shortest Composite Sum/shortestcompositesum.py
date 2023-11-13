#64
# n=int(input())
# print(2)
# if n%2:print(9,n-9)
# else:print(4,n-4)

#rewrite the above code to only use one print statement
#this is the code I wrote

#67
# n,p=int(input()),print
# p(2),p(9 if n%2 else 4,n-9 if n%2 else n-4)

# #61
# n=int(input())
# a=5*(n%2)
# print(2,'\n',4+a,' ',n-4-a,sep='')

# #52
# n=int(input())
# print(2);a=5*(n%2)
# print(4+a,n-4-a)

#57
# n=int(input())
# print('2\n',4+5*n%2,' ',n-4-5*n%2,sep='')

#53
# n,p=int(input()),print
# p(2),p(4+5*(n%2),n-4-5*(n%2))

#49
n,p=int(input()),print
p(2),p(4+n%2*5,n-4-n%2*5)