o=input()
n=len(o)
h,u,g=o.count('_')/n,sum(map(str.islower,o))/n,sum(map(str.isupper,o))/n
print(h,u,g,1-h-u-g,sep='\n')

#-----------------------------------------------

string = input()
length = len(string)
whitespaces = string.count('_')/length
lowercase = sum(map(str.islower, string))/length
uppercase = sum(map(str.isupper, string))/length
symbols = 1-whitespaces-lowercase-uppercase
print(whitespaces)
print(lowercase)
print(uppercase)
print(symbols)


i=input()
n=len(i)
w=i.count('_')/n
l=[sum(ord(c)>96 and ord(c)<123)for c in i]/n
u=[sum(ord(c)>64 and ord(c)<91)for c in i]/n
print(w,l,u,1-w-l-u,sep='\n')

#list of ascii values between 33 and 126
#33-47: !"#$%&'()*+,-./
#48-57: 0123456789
#58-64: :;<=>?@
#65-90: ABCDEFGHIJKLMNOPQRSTUVWXYZ
#91-96: [\]^_`
#97-122: abcdefghijklmnopqrstuvwxyz
#123-126: {|}~
