_ = input()
words = list(input().split())
sol = ""
for word in words:
    if word[0] in "AZERTYUIOPQSDFGHJKLMWXCVBN":
        sol += word[0]
print(sol)