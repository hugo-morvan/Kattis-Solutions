t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # number of stores
    positions = list(map(int, input().split()))  # parking positions
    
    # calculate the minimum and maximum parking distances
    min_dist = min(positions)
    max_dist = max(positions)
    
    # output the total distance travelled by the customer
    print((max_dist - min_dist) * 2)
