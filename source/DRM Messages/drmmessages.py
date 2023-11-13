import string

# Rotate the letters in a string by a given amount
def rotate(s, amount):
    return ''.join([string.ascii_uppercase[(string.ascii_uppercase.index(c) + amount) % 26] for c in s])

# Split a string in half and return the two halves
def split_in_half(s):
    n = len(s)
    return s[:n//2], s[n//2:]

# Main function to solve the problem
def drmmessages():
    # Read input
    message = input().strip()

    # Split the message in half
    first_half, second_half = split_in_half(message)

    # Rotate each half by the sum of their letter values
    first_sum = sum([string.ascii_uppercase.index(c) for c in first_half])
    second_sum = sum([string.ascii_uppercase.index(c) for c in second_half])
    rotated_first_half = rotate(first_half, first_sum)
    rotated_second_half = rotate(second_half, second_sum)

    # Merge the two halves by rotating each letter by the value of the corresponding letter in the other half
    result = ''.join([rotate(rotated_first_half[i], string.ascii_uppercase.index(rotated_second_half[i])) for i in range(len(rotated_first_half))])
    print(result)

# Call the main function
drmmessages()
