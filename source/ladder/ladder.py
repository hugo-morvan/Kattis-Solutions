import math

height, angle = map(int, input().split())

# Convert the angle from degrees to radians
angle_rad = math.radians(angle)

# Compute the ladder length using trigonometry
ladder_length = height / math.sin(angle_rad)

# Round up to the nearest integer and print the result
print(math.ceil(ladder_length))
