daysOfWeek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Read input
day, month = map(int, input().split())

# Use Zeller's congruence formula
q = day
m = month
if m < 3:
    m += 12
    year = 2009 - 1
else:
    year = 2009
k = year % 100
j = year // 100
h = (q + 13*(m+1)//5 + k + k//4 + j//4 + 5*j) % 7

# Print result
print(daysOfWeek[h])
