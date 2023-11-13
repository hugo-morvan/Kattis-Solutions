print(int(bin(int(input()))[2:][::-1],2))

num = int(input()) # get the number

binary = bin(num)[2:] # [2:] to chop off the "0b" part

reverse = binary[::-1] # reverse the string

print(int(reverse,2)) # convert back to an int from a base 2 number
