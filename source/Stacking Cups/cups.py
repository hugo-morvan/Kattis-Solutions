n = int(input())

circles = []
for i in range(n):
    circle = input().split()
    if circle[0].isnumeric():
        radius = int(circle[0]) / 2
        color = circle[1]
    else:
        radius = int(circle[1])
        color = circle[0]
    circles.append((radius, color))

circles.sort()
for circle in circles:
    print(circle[1])
