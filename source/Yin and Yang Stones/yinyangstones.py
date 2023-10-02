stones = input()
w_count = stones.count('W')
b_count = stones.count('B')

if w_count == b_count:
    print(1)
else:
    print(0)
