d,x,y,h=map(int,input().split())
from math import *
print((tan(atan(y/x)-atan((y-h/2)/x))+tan(atan((y+h/2)/x)-atan(y/x)))*d)