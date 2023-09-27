n , target = map(int, input().split())
dict ={}
for _ in range(n):
    key, val = input().split()
    dict[key] = int(val)

letters = []
for k in dict.keys(): # [ab, ba, bd, db, bc]
    x,y = k[0], k[1]
    letters.append(x)
    letters.append(y)
letters = sorted([*set(letters)] )# 
INF = 10**9
table = [[INF]*(target) for _ in range(len(letters))]

#initialization
for l in range(len(letters)): 
    table[l][0] = 0
# Fill the table in bottom up manner   
for i in range(1,target): # For all values from 1 to target
    
    for j in range(len(letters)): # For all letters in a column
        
        for key in dict.keys(): # For all keys in the dictionary
            first, second = key[0], key[1]
            if second == letters[j]: # If the first letter of the key is the same as the letter in the column
                cost = dict[key]
                table[j][i] = min(table[j][i], table[letters.index(first)][i-1] + cost) 
                
#print the minimum value of the last row of the table
last_col = [table[i][-1] for i in range(len(letters))]
print(min(last_col))
