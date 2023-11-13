#104
#import math
#n,d=map(int,input().split("/"))
#n=5*n-160*d
#d*=9
#g=math.gcd(n,d)
#print(n//g,d//g,sep="/")
#
##103
#import math
#n,d=map(int,input().split("/"))
#n=5*n-160*d;g=math.gcd(n,d*9)
#print(n//g,d*9//g,sep="/")
#
##102
#import math
#n,d=map(int,input().split("/"))
#n=5*n-160*d;g=math.gcd(n,d*9);print(n//g,d*9//g,sep="/")
#
#Stupid python
#n,d=map(float,input().split("/"))
#n=5*n-160*d
#d*=9
#a,b=(n/d).as_integer_ratio()
#print(a,b,sep="/")

import math
n,d=map(int,input().split("/"))
n=5*n-160*d;g=math.lcm(n,d*9);print(n/g,d*9/g,sep="/")