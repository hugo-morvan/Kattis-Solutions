n = int(input())
Noabsent = True
first = input()
for i in range(n-1):
    second = input()
    if second != "Present!" and first !="Present!":
        print(first)
        Noabsent = False
    first = second
if first != "Present!":
    print(first)
    Noabsent = False
if Noabsent: print("No Absences")