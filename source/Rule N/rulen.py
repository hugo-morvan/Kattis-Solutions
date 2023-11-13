n,l,r = input().split()
r = int(r)
start = input()
patterns = ["111","110","101","100","011","010","001","000"]
rule = bin(int(n))[2:]
rule = rule.zfill(8) #pad with 0s in front to make 8 digits
start = "0"*int(r+1) + start + "0"*int(r+1)
def calculate_next_state(patterns, rule, start):
    next_state = ""
    for i in range(1, len(start)-1):
        pat = start[i-1:i+2]
        index = patterns.index(pat)
        next_state += rule[index]
    return next_state
for i in range(r+1):
    start = calculate_next_state(patterns, rule, start)
    print(start[r-i:i-r])
