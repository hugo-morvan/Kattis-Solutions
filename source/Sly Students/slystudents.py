import math

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

words = input().split(" ")
for word in words:
    vals = []
    for let in word:
        val = ord(let)
        vals.append(val)
    #find the gcd of the list of values
    gcd = vals[0]
    for i in range(len(vals)):
        gcd = math.gcd(gcd, vals[i])
    print(gcd)
    for i in range(len(vals)):
        vals[i] = vals[i]//gcd
        #print number in base 3
        print(ternary(vals[i]), end=" ")
    print()

#print possible or impossible with 50% chance
