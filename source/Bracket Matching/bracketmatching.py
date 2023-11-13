n=int(input())
par = 0
square = 0
curly = 0
bool = True

s = input()
for j in s:
    if j == '(':
        par += 1
    elif j == ')':
        par -= 1
    elif j == '[':
        square += 1
    elif j == ']':
        square -= 1
    elif j == '{':
        curly += 1
    elif j == '}':
        curly -= 1
    if par < 0 or square < 0 or curly < 0:
        bool = False
if par == 0 and square == 0 and curly == 0 and bool:
    print('Valid')
else:
    print('Invalid')
