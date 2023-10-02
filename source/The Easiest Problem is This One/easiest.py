def digit_sum(n):
    return sum(map(int, str(n)))

while True:
    n = int(input())
    if n == 0:
        break

    target = digit_sum(n)
    p = 11
    while digit_sum(p * n) != target:
        p += 1

    print(p)
