def is_harshad(n):
    # Compute the sum of the digits of n
    digit_sum = sum(int(d) for d in str(n))
    
    # Check if n is divisible by the sum of its digits
    return n % digit_sum == 0

# Read in the input number
n = int(input())

# Increment n until we find a Harshad number
while not is_harshad(n):
    n += 1

# Print the smallest Harshad number greater than or equal to n
print(n)
