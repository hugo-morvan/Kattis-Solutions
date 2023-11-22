n = int(input())
hotels_distances = list(input().split())
dice_rolls = {"2":1/36, "3":2/36, "4":3/36 ,"5":4/36 ,"6":5/36,"7":1/6,"8":5/36,"9":4/36,"10":3/36,"11":2/36,"12":1/36}
prob = 0
for h in hotels_distances:
    prob += dice_rolls[h]
print(prob)
