def root_of_square(n, lo, hi):
    while True:
        mid = lo + (hi - lo) // 2
        sq = mid * mid
        if sq == n:
            return mid
        elif sq < n:
            lo = mid + 1
        else:
            hi = mid - 1

if __name__ == '__main__':
    n = int(input())
    buffer = [''] * 20002  # buffer1: 0-10000, buffer2: 10001-20001
    out = buffer[10001:]   # <--buffer2
    while n > 0:
        index = 0
        buffer = input()
        length = len(buffer)
        sqr = root_of_square(length, 1, 100)

        # Iterations take care of encoding
        # (sqr-1) + (2sqr-1) + ...
        # (sqr-2) + (2sqr-2) + ...
        # ...
        for i in range(sqr - 1, -1, -1):
            for j in range(i, length, sqr):
                out[index] = buffer[j]
                index += 1

        out[index] = '\0'
        print(''.join(out))
        n -= 1
