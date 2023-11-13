import math as m
n=float(input())
print(m.exp(1/n*m.log(n)))

from math import exp,log
n=float(input())
print(exp(log(n)/n))


from math import log10
n=float(input())
print(10**(log10(n)/n))
