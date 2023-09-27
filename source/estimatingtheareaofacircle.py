import math

while True:
    r, m, c = map(float, input().split())
    if r == m == c == 0:
        break
    true_area = math.pi * r ** 2
    estimated_area = 4 * r ** 2 * c / m
    print(true_area, estimated_area)
