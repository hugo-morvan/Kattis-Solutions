sides = list(map(int, input().split()))

# Sort the sides in ascending order
sides.sort()

# Calculate the area of the rectangle
area = sides[0] * sides[2]

print(area)
