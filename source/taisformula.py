n = int(input())
prev_t, prev_v = map(float, input().split())
sum = 0.0
while n > 1:
    curr_t, curr_v = map(float, input().split())
    sum += (prev_v + curr_v) / 2.0 * (curr_t - prev_t)
    prev_t = curr_t
    prev_v = curr_v
    n -= 1
print("{:.6f}".format(sum / 1000.0))