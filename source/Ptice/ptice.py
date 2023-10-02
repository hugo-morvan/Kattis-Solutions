n = int(input())
s = input()

adrian = 'ABC' * ((n // 3) + 1)
adrian = adrian[:n]

bruno = 'BABC' * ((n // 4) + 1)
bruno = bruno[:n]

goran = 'CCAABB' * ((n // 6) + 1)
goran = goran[:n]

score = {'Adrian': 0, 'Bruno': 0, 'Goran': 0}

for i in range(n):
    if s[i] == adrian[i]:
        score['Adrian'] += 1
    if s[i] == bruno[i]:
        score['Bruno'] += 1
    if s[i] == goran[i]:
        score['Goran'] += 1

max_score = max(score.values())

print(max_score)
for person, value in score.items():
    if value == max_score:
        print(person)
