word = input()
v = 0
y = 0
for c in word:
    if c in {'a','e','i','o','u'}:v+=1
    if c=='y':y+=1
print(v,v+y)