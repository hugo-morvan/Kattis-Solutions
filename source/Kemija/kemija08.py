vowels = ['a', 'e', 'i', 'o', 'u']
s = input()
decoded = ''
i = 0
while i < len(s):
    decoded += s[i]
    if s[i] in vowels:
        i += 3
    else:
        i += 1

print(decoded)
