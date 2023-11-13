def ssd(n, b):
    sum_of_squares = 0
    while n > 0:
        remainder = n % b
        sum_of_squares += remainder ** 2
        n //= b
    return sum_of_squares

for i in range(int(input())):
    k,b,n=input().split()
    print(k,ssd(int(n),int(b)))