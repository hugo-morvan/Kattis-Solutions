import math

# Read in the four sides
a, b, c, d = map(int, input().split())

# Calculate the semiperimeter
s = (a + b + c + d) / 2

# Calculate the area using Heron's formula
area = math.sqrt((s-a)*(s-b)*(s-c)*(s-d))

print(area)
