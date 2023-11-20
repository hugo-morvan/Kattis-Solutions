#=== Work in Progress ===============
ef cst(n):
    #returns the sequence CST(n)
    #n/2 if n even, 3n+1 if n is odd
    seq = []
    while n!= 1:
        seq.append(n)
        if n%2==0:
            n/=2
        else:
            n = 3*n+1
    seq.append(1)
    return seq

x = input()
valid = True
#the sequence contains only E’s and O’s, ends in O and no two O’s are adjacent.
for char in x:
    if char!='E' and char!='O':
        valid=False
        break
if x[-1] != 'O': valid=False
if x.__contains__("OO"): valid=False
if valid:
    #return a single decimal integer, n, such that n is the smallest integer 
    # for which CST(n) is the input sequence. 
    # Input will be chosen such that n<= 2^47



    print("temp")
else:
    print("INVALID")
