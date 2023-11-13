import sys
def w(n):
 p=True
 while n>1:
  d,m=divmod(n,[2,9][p])
  n = d+1 if m else d
  p = not p
 return ['Stan wins.','Ollie wins.'][p]
print('\n'.join(w(int(l)) for l in sys.stdin.readlines()))