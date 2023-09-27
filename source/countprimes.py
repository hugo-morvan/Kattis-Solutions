import math

def count_primes(n):
    if n <= 1:
        return 0
    else:
        primes = [2]
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        primes += [i for i in range(2, n + 1) if sieve[i]]
        return len(primes)
        

n = int(input())
print(count_primes(n))